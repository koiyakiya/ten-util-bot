import aiosqlite
from pathlib import Path
from collections.abc import Iterable
from typing import Any, Optional
from .sql import *
from . import __DEBUG_DB_PATH__
import os


class Database:
    __slots__ = (
        "path",
        "conn",
    )

    def __init__(self, path: Path) -> None:
        self.path = path
        self.conn: Optional[aiosqlite.Connection] = None

    async def connect(self) -> aiosqlite.Connection:
        if self.conn is None:
            self.conn = await aiosqlite.connect(self.path)
        return self.conn

    async def create(self) -> None:
        """Never use outside of `__main__.py`"""
        await self.exec(CREATE_TABLE)

    async def exec(
        self, sql: str, parameters: Optional[Iterable[Any]] | None = None
    ) -> aiosqlite.Cursor:
        """
        Very similar to aiosqlite's `execute` function, although this one commits before returning,
        to remove that extra annoying step.
        """
        if parameters is None:
            parameters = []
        cursor = await self.conn.execute(sql, parameters)
        await self.conn.commit()
        return cursor

    async def sel(
        self, sql: str, parameters: Optional[Iterable[Any]] | None = None
    ) -> aiosqlite.Cursor:
        """
        Exactly the same as aiosqlite's `execute` function, although
        I named it "sel" for better readability.
        """
        if parameters is None:
            parameters = []
        cursor = await self.conn.execute(sql, parameters)
        return cursor

    async def close(self) -> None:
        if self.conn:
            await self.conn.close()
            self.conn = None

    async def _delete(self) -> None:
        """WARNING! Only use when changing variable `wipe` in `__init__.py`."""
        if os.path.exists(__DEBUG_DB_PATH__):
            os.remove(__DEBUG_DB_PATH__)

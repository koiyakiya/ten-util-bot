import logging
import arc
import hikari as hk
from ..db import Database
from ..sql import *

_log = logging.getLogger(__name__)

plugin = arc.GatewayPlugin("KneelModule")

@plugin.listen()
@plugin.inject_dependencies
async def kneel_reaction_added(
    event: hk.GuildReactionAddEvent,
    db: Database = arc.inject(),
    rest: hk.api.RESTClient = arc.inject(),
) -> None:
    gid: hk.Snowflake = event.guild_id
    cid: hk.Snowflake = event.channel_id
    msg: hk.Message = await rest.fetch_message(gid, cid)
    async with db.sel(SELECT_KNEEL_ADD) as cur:
        res = await cur.fetchone()
    _log.debug(res)
    db.exec(INSERT_INTO_KNEEL_ADD, gid, msg.member.id, msg.member.display_name, 1)
    
@arc.loader
def loader(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)

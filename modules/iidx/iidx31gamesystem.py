from time import time
import config
from fastapi import APIRouter, Request, Response
from core_common import core_process_request, core_prepare_response, E

router = APIRouter(prefix="/local2", tags=["local2"])
router.model_whitelist = ["LDJ"]

@router.post("/{gameinfo}/IIDX31gameSystem/systemInfo")
async def iidx31gameSystem_systeminfo(request: Request):
    request_info = await core_process_request(request)

    unlock = ()
    # force unlock LM exclusives to complete unlock all songs server side
    # this makes LM exclusive folder disappear, so just use hex edits
    # unlock = (28073, 28008, 29095, 29094, 29027, 30077, 30076, 30098, 30106, 30107, 30028, 30064, 30027)

    current_time = round(time())

    response = E.response(
        E.IIDX31gameSystem(
            status="0",
            CommonBossPhase="1",
            isNewSongAnother12OpenFlg="1",
            OldBPLBattleOpenPhase="1"
        )
    )

    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)
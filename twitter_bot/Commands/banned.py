import json
import logging

import functions
import requests as req
from config import token
from easter_eggs import special_cases_dict


def check_if_banned(player_name) -> dict:
    hiscore_url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={player_name}"
    hiscores_r = req.get(hiscore_url)

    if hiscores_r.status_code == 404:

        url = (
            f"https://apps.runescape.com/runemetrics/profile/profile?user={player_name}"
        )
        runemetrics_r = req.get(url)

        if runemetrics_r.status_code == 200:

            data = runemetrics_r.text
            runemetrics_data = json.loads(data)

            status = runemetrics_data.get("error")

            if status == "NOT_A_MEMBER":
                return {"name": player_name, "banned": True}
            else:
                return {"name": player_name, "banned": "Maybe?"}

    elif hiscores_r.status_code == 200:
        return {"name": player_name, "banned": False}

    return {"name": player_name, "banned": "ERROR"}


def banstatus(rsn):
    if functions.is_valid_rsn(rsn):
        try:
            response = [v for k, v in special_cases_dict.items() if rsn.find(k) == 0][0]
            return response
        except IndexError:
            try:
                print(f"Trying to get ban status for {rsn}")
                r = check_if_banned(rsn)

                if r["banned"]:
                    response = f"""🧙 ❌ {r['name']} has been banned or does not appear on the Hiscores ❌"""
                else:
                    response = f"""🧙 ✔️ {r['name']} has not been banned ✔️"""

                return response

            except:
                pass
    else:
        response = "The system could not detect a valid RSN. Please send your message again using a valid RSN."
        return response

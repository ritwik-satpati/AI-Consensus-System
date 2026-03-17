# main.py
MODULE_NAME = "MAIN"

import asyncio
from ai_consensus_system_m1 import run_ai_consensus_system_m1
from ai_consensus_system_m2 import run_ai_consensus_system_m2
from test import test

if __name__ == "__main__":
    # asyncio.run(run_ai_consensus_system_m1())
    asyncio.run(run_ai_consensus_system_m2())
    # test()
    pass
# main.py
MODULE_NAME = "MAIN"

import asyncio
from ai_consensus_system import run_ai_consensus_system
from test import test

if __name__ == "__main__":
    asyncio.run(run_ai_consensus_system())
    # test()
    pass
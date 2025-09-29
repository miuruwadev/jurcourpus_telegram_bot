import asyncio
from config import MODE

if __name__ == "__main__":
    if MODE == 'DEVELOPMENT':
        from bot import main
        asyncio.run(main())

    else:
        from watcher import main
        main()

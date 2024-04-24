from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler(timezone="Asia/kolkata")
import asyncio

async def job():
    print('hi')


scheduler.add_job(job, "interval", seconds=3)

scheduler.start()

asyncio.get_event_loop().run_forever()
from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler(timezone="Asia/kolkata")
import asyncio

async def job():
    print('hi')


scheduler.add_job(job, "interval", seconds=3)



loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
scheduler.start()
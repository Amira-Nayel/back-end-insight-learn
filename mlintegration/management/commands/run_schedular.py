import schedule
import time
import signal
import sys
from django.core.management.base import BaseCommand
from mlintegration.views import get_predictions  # Adjust the import based on your app structure

class Command(BaseCommand):
    help = 'Run the scheduler to fetch predictions'

    def handle(self, *args, **kwargs):
        def run_scheduler():
            # Schedule the task to run every minute
            schedule.every(7).days.do(get_predictions)

            while True:
                schedule.run_pending()
                time.sleep(1)

        def signal_handler(sig, frame):
            print('Stopping the scheduler...')
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        run_scheduler()
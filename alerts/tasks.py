import logging

logger = logging.getLogger(__name__)

def check_price():
    try:
        # ... price checking logic

        for alert in alerts:
            try:
                send_mail(
                    'Price Alert',
                    f'The price of Bitcoin has reached your target price of {alert.target_price}.',
                    'vdkalife@gmail.com',
                    [alert.email],
                    fail_silently=False,
                )
                alert.status = 'triggered'
                alert.save()
            except Exception as e:
                logger.error(f"Error sending email for alert {alert.id}: {e}")

    except Exception as e:
        logger.error(f"Error in check_price task: {e}")

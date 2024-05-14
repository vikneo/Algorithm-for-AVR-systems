from django.core.mail import send_mail

from models import Order
from system_avr.settings import EMAIL_HOST_USER

from celery import task




@task
def order_created(order_id):
    """
    Задача для отправки сообщения на почту при оформлении заявки
    """
    order = Order.objects.get(id=order_id)
    subject = f"Заявка №-{order.id}"
    message = f"Оформлена заявка с №-{order.id}.\n \
        Проект: ID-{order.id_product}.\n \
        Объект: {order.subject}.\n"
    
    mail_send = send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[EMAIL_HOST_USER, ]
    )

    return mail_send

from django.core.mail import send_mail

from celery import task

from models import Order


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
        subject,
        message,
        'v.martynov@rineco.ru'
    )

    return mail_send

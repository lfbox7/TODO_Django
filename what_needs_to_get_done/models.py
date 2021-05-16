from django.db import models


class Task(models.Model):
    COMPLETED = 'Completed'
    IN_PROGRESS = 'In progress'
    NOT_STARTED = 'Not started'
    OVERDUE = 'Overdue'
    STATUS_CHOICES = (
        (COMPLETED, 'Completed'),
        (IN_PROGRESS, 'In progress'),
        (NOT_STARTED, 'Not started'),
        (OVERDUE, 'Overdue'),
    )

    title = models.TextField()
    due_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    status = models.TextField(choices=STATUS_CHOICES, default=NOT_STARTED)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title
    '''
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})
    '''
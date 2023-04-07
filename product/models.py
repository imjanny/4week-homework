from django.db import models


class Product(models.Model):
    # """
    # 상품 모델입니다.
    # 상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    # """
    code = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    stock_quantity = models.IntegerField(default=0)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)

    def __str__(self):
        return str(self.code)

    def save(self, *args, **kwargs):
        if not self.pk:  # 새로운 상품이 생성될 때
            self.stock_quantity = 0  # stock_quantity를 0으로 초기화
        super().save(*args, **kwargs)


class Inbound(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.product.stock_quantity += self.quantity - self.pk if self.pk else self.quantity
        super().save(*args, **kwargs)




class Outbound(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.product.stock_quantity -= self.quantity
        super().save(*args, **kwargs)

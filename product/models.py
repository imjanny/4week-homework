from django.db import models

#제품의 기본이 되는 제품 클래스
class Product(models.Model):
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
    
#제품을 저장하는 메소드
    def save(self, *args, **kwargs):
        if not self.pk:  # 새로운 상품이 생성될 때
            self.stock_quantity = 0  # stock_quantity를 0으로 초기화
        super().save(*args, **kwargs)

#입고 클래스
class Inbound(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
# 제품 입고를 저장하는 메소드
    def save(self, *args, **kwargs):
        self.product.stock_quantity += self.quantity - self.pk if self.pk else self.quantity
        super().save(*args, **kwargs)



#제품 출고 클래스
class Outbound(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
#제품 출고를 저장하는 메소드
    def save(self, *args, **kwargs):
        self.product.stock_quantity -= self.quantity
        super().save(*args, **kwargs)

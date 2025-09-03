import uuid
from django.db import models

class News(models.Model): #models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django. #News adalah nama model yang kamu definisikan.
    CATEGORY_CHOICES = [ #CATEGORY_CHOICES adalah tuple yang mendefinisikan pilihan kategori berita yang tersedia.
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #id adalah field bertipe UUIDField yang digunakan sebagai primary key dan nilainya di-generate otomatis menggunakan uuid.uuid4
    title = models.CharField(max_length=255) #title adalah field bertipe CharField untuk judul berita, dengan panjang maksimal 255 karakter.
    content = models.TextField() #content adalah field bertipe TextField untuk isi berita yang dapat menampung teks panjang.
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update') #category adalah field bertipe CharField dengan pilihan terbatas sesuai CATEGORY_CHOICES, dengan nilai default 'update'.
    thumbnail = models.URLField(blank=True, null=True) #thumbnail adalah field bertipe URLField untuk menyimpan URL gambar thumbnail berita (opsional).
    news_views = models.PositiveIntegerField(default=0) #news_views adalah field bertipe PositiveIntegerField yang menyimpan jumlah view berita, dengan nilai default 0.
    created_at = models.DateTimeField(auto_now_add=True) #created_at adalah field bertipe DateTimeField yang otomatis berisi tanggal dan waktu saat data dibuat.
    is_featured = models.BooleanField(default=False) #is_featured adalah field bertipe BooleanField untuk menandai apakah berita ini ditampilkan sebagai berita unggulan.
    
    def __str__(self): #Method __str__ digunakan untuk mengembalikan representasi string dari objek (dalam hal ini judul berita).
        return self.title
    
    @property
    def is_news_hot(self): #Decorator @property digunakan untuk membuat atribut read-only yang nilainya merupakan hasil perhitungan dari atribut lain. Dalam kasus ini, is_news_hot akan bernilai True jika jumlah view berita lebih dari 20.
        return self.news_views > 20
        
    def increment_views(self): #Method increment_views() digunakan untuk menambah jumlah view berita sebesar 1 dan menyimpan perubahan ke database.
        self.news_views += 1
        self.save()
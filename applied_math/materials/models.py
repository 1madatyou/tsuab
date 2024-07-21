from django.db import models


class DiplomaThesis(models.Model):
    """Модель дипломной работы"""

    title = models.CharField(verbose_name="Тема", max_length=255)
    file = models.FileField(verbose_name="Файл", upload_to="theses")
    date_upload = models.DateTimeField(verbose_name="Дата загрузки", auto_now_add=True)

    class Meta:
        verbose_name_plural = "дипломные работы"
        verbose_name = "дипломная работа"

    def get_formatted_date_upload(self):
        return self.date_upload.strftime("%d.%m.%Y")

    def __str__(self):
        return self.title


class Manual(models.Model):
    """Модель методического указания"""

    title = models.CharField(verbose_name="Тема", max_length=255)
    file = models.FileField(verbose_name="Файл", upload_to="theses")

    author_surname = models.CharField(verbose_name="Фамилия автора", max_length=255)
    author_name = models.CharField(verbose_name="Имя автора", max_length=255)
    author_patronymic = models.CharField(verbose_name="Отчество автора", max_length=255)

    date_upload = models.DateTimeField(verbose_name="Дата загрузки", auto_now_add=True)

    class Meta:
        verbose_name_plural = "методические указания"
        verbose_name = "методическое указание"

    def get_formatted_date_upload(self):
        return self.date_upload.strftime("%d.%m.%Y")

    def get_formatted_author_full_name(self):
        return (
            f"{self.author_surname} {self.author_name[0]}.{self.author_patronymic[0]}"
        )

    def __str__(self):
        return self.title


class EducationalMaterial(models.Model):
    """Модель учебных материалов"""

    title = models.CharField(verbose_name="Тема", max_length=255)

    class Meta:
        verbose_name_plural = "обучающие материалы"
        verbose_name = "материал для обучения"


class EducationalMaterialItem(models.Model):
    """Модель содержимого учебного материала"""

    title = models.CharField(verbose_name="Название", max_length=255)

    date_upload = models.DateTimeField(verbose_name="Дата загрузки", auto_now_add=True)

    def get_formatted_date_upload(self):
        return self.date_upload.strftime("%d.%m.%Y")

    class Meta:
        abstract = True


class EducationalMaterialLink(EducationalMaterialItem):
    material = models.ForeignKey(
        "materials.EducationalMaterial", related_name="links", on_delete=models.CASCADE
    )
    href = models.URLField(verbose_name="Ссылка")

    class Meta:
        verbose_name_plural = "ссылки"
        verbose_name = "ссылка"


class EducationalMaterialFile(EducationalMaterialItem):
    material = models.ForeignKey(
        "materials.EducationalMaterial", related_name="files", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="educational_materials", verbose_name="Файл")

    class Meta:
        verbose_name_plural = "файлы"
        verbose_name = "файл"

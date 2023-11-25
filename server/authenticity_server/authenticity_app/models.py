

# authenticity_app/models.py
from django.db import models

class VideoAnalysis(models.Model):
    video_file = models.FileField(upload_to='videos/')
    confidence_score = models.FloatField()
    result_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.video_file.name}"


from rest_framework import serializers
from main.models import Author, Theme, Poem

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]
    
class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ["id", "name"]
    
class PoemSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True
    )
    theme = serializers.PrimaryKeyRelatedField(
        queryset=Theme.objects.all(), write_only=True
    )

    authorDetails = AuthorSerializer(source="author", read_only=True)
    themeDetails = ThemeSerializer(source="theme", read_only=True)

    class Meta:
        model = Poem
        fields = ["id", "name", "author", "authorDetails", "theme", "themeDetails"]
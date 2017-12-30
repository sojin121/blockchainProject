from django.shortcuts import render
from .models import File
from .models import Post
from django.utils import timezone
from .forms import PostForm
from .forms import UploadFiles
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
# Create your views here.


def post_list(request):
    posts = Post.objects.filter()
    return render(request, 'blockchain/post_list.html', {'posts': posts})


def uploaded_file_list(request):
    files = File.objects.filter()
    return render(request, 'blockchain/UploadedFileList.html',{'files': files})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blockchain/post_edit.html', {'form': form})


def upload_files(request):
    if request.method == "POST":
        files = UploadFiles(request.POST)
        if files.is_valid():
            upload = files.save(commit=False)
            upload.upload_date = timezone.now()
            upload.save()
            return redirect('file_detail', pk=files.pk)
    else:
        files = UploadFiles()
        return render(request, 'blockchain/UploadFiles.html', {'files': files})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blockchain/post_detail.html', {'post': post})


def file_detail(request, pk):
    files = get_object_or_404(File, pk=pk)
    return render(request, 'blockchain/FileDetail.html', {'files': files})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blockchain/post_edit.html', {'form': form})


def upload_edit(request, pk):
    files = get_object_or_404(File, pk=pk)
    if request.method == "POST":
        form = UploadFiles(request.POST, instance=files)
        if form.is_valid():
            files = form.save(commit=False)
            files.upload_date = timezone.now()
            files.save()
            return redirect('file_detail', pk=files.pk)
    else:
        form = UploadFiles(instance=files)
    return render(request, 'blockchain/FilesDetail.html', {'files': files})

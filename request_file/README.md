## Request Files

You can define files to be uploaded by the client using File.

###### **INFO**

To receive uploaded files, first install [python-multipart](https://github.com/Kludex/python-multipart).

```console
pip install python-multipart
```

This is because uploaded files are sent as "form data".

## For the small file

- Use `File()`

## For the large file

- Use `UploadFile()`

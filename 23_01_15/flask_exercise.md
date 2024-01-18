

## Övning: Flask
Din uppgift är att bygga en todo-list med hjälp av Flask. Alla "To-Do" ska ligga i en fil som heter tasks.json. Se exempelfilen.

Du ska göra ett API i Flask som läser data från filen `tasks.json` och modifierar denna vid vissa requests.

### Endpoints

`GET /tasks` Hämtar alla tasks. För VG: lägg till en parameter `completed` som kan filtrera på färdiga eller ofärdiga tasks.

`POST /tasks` Lägger till en ny task. Tasken är ofärdig när den först läggs till.

`GET /tasks/{task_id}` Hämtar en task med ett specifikt id.

`DELETE /tasks/{task_id}` Tar bort en task med ett specifikt id.

`PUT /tasks/{task_id}` Uppdaterar en task med ett specifikt id.

`PUT /tasks/{task_id}/complete` Markerar en task som färdig.

`GET /tasks/categories/` Hämtar alla olika kategorier.

`GET /tasks/categories/{category_name}` Hämtar alla tasks från en specifik kategori.
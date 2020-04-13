
# WareHouse Management And Analytics (Inventory type)
#### WareHouse Management System is an online system that is used to manage the selling and stocks of a company. It also manages its various dealers and the products that they sell. It manages bills generated and shows profit earned and displays various graphs for better understanding. It is build using Django framework in Python along with Java Script,HTML and CSS. It uses MySql Server for storing data in database .
#

<video src="https://www.youtube.com/watch?v=qoyfiI1tXs4" poster="poster.jpg" width="320" height="200" controls preload></video>

### For framework setup see this video : https://www.youtube.com/watch?v=VuETrwKYLTM&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau&index=2
#
### For more help for database refer: https://www.youtube.com/watch?v=69YkZqZgz9s&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau&index=18
#
### After setup of database
run following commands in terminal of path to project folder
In pycharm you can directly access terminal
commands :
```
python manage.py makemigrations
python manage.py sqlmigrate Main_Inventory 001
python migrate
```
#
#### One last step : Install pymysql by following command
``` pip install pymysql ```

Now go to following path in your computer:

C:\Users\ {Your-username-folder} \AppData\Local\Programs\Python\Python38-32\Lib\site-packages\pymysql\

Replace __init__.py file with uploaded pymysql\__init__.py file.(You can find new __init__.py file in pymysql folder)

#
## You can download preview video from here :https://github.com/Deep-Menpara/Inventory/blob/master/Application%20Preview(DEMO%20VIDEO).mp4

#

## For any Queries you can refer : https://docs.djangoproject.com/en/3.0/intro/tutorial01/




## Screenshots

### Registration for new dealer or employee who sells items
![Screenshot (44)](https://user-images.githubusercontent.com/30389552/79066298-75d49b00-7cd4-11ea-8355-7b8c54576b3e.png)

#

### Home Shows company profit graph and Stock of products
![Screenshot (38)](https://user-images.githubusercontent.com/30389552/79066313-a3214900-7cd4-11ea-94f2-2bd489fe6219.png)

#

### Product / stock details
![Screenshot (39)](https://user-images.githubusercontent.com/30389552/79066328-c21fdb00-7cd4-11ea-82b2-0f0b85d47eda.png)

#

### Add new product : You can add new quantity of existing stock or a new item
![Screenshot (40)](https://user-images.githubusercontent.com/30389552/79066340-d2d05100-7cd4-11ea-8eac-f5ca7dd2dd2b.png)

#

### Sell Product by adding items in cart
![Screenshot (41)](https://user-images.githubusercontent.com/30389552/79066357-e54a8a80-7cd4-11ea-999e-bcb4e638d5fd.png)

#

### Profit graph : Shows profit made by Logged in user
![Screenshot (42)](https://user-images.githubusercontent.com/30389552/79066385-2773cc00-7cd5-11ea-9b7b-d78d70fc400f.png)

#

### History : Detailed Selling history of user
![Screenshot (43)](https://user-images.githubusercontent.com/30389552/79066408-55f1a700-7cd5-11ea-8c5c-80b1c803dbed.png)

#


Thank You!!!

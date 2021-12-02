---
layout: default
title: 01 - Python and APIs
parent: Topic 08 - Making Web Requests
grand_parent: Lectures
nav_order: 1
---
# Python & APIs: A Winning Combo for Reading Public Data

[Source](https://realpython.com/python-api/)

Knowing how to consume an API is one of those magical skills that, once mastered, will crack open a whole new world of possibilities, and consuming APIs using Python is a great way to learn such a skill.

A lot of apps and systems you use on a daily basis are connected to an API. From very simple and mundane things, like checking the weather in the morning, to more addictive and time-consuming actions, such as scrolling through your Instagram, TikTok, or Twitter feed, APIs play a central role.

In this tutorial, you’ll learn:

* What an API is
* How you can consume APIs with your Python code
* What the most important API-related concepts are
* How to use Python to read data available through public APIs

By the end of this tutorial, you’ll be able to use Python to consume most APIs you come across. If you’re a developer, knowing how to consume APIs with Python will make you much more proficient, especially when it comes to integrating your work with third-party applications.

> Note: This tutorial is focused on how to consume APIs using Python, not how to build them. For information on building an API with Python, check out [Python REST APIs With Flask, Connexion, and SQLAlchemy](https://realpython.com/flask-connexion-rest-api/).

## Getting to Know APIs

API stands for application programming interface. In essence, an API acts as a communication layer, or as the name says, an interface, that allows different systems to talk to each other without having to understand exactly what each other does.

APIs can come in many forms or shapes. They can be operating system APIs, used for actions like turning on your camera and audio for joining a Zoom call. Or they can be web APIs, used for web-focused actions such as liking images on your Instagram or fetching the latest tweets.

No matter the type, all APIs function mostly the same way. You usually make a request for information or data, and the API returns a response with what you requested. For example, every time you open Twitter or scroll down your Instagram feed, you’re basically making a request to the API behind that app and getting a response in return. This is also known as calling an API.

In this tutorial you’ll focus more on the high-level APIs that communicate across networks, also called web APIs.

### SOAP vs REST vs GraphQL

Even though some of the examples mentioned above are geared toward newer platforms or apps, web APIs have been around for quite a long time. In the late 1990s and early 2000s, two different design models became the norm in exposing data publicly:

* **SOAP (Simple Object Access Protocol)** is typically associated with the enterprise world, has a stricter contract-based usage, and is mostly designed around actions.
* **REST (Representational State Transfer)** is typically used for public APIs and is ideal for fetching data from the web. It’s much lighter and closer to the HTTP specification than SOAP.

Nowadays, there’s a new kid in town: [GraphQL](https://graphql.org/). Created by Facebook, GraphQL is a very flexible query language for APIs, where the clients decide exactly what they want to fetch from the server instead of the server deciding what to send.

If you want to learn more about the differences between these three design models, then here are a few good resources:

* [What is SOAP?](https://www.altexsoft.com/blog/engineering/what-is-soap-formats-protocols-message-structure-and-how-soap-is-different-from-rest/)
* [What is REST?](https://restfulapi.net/)
* [API 101: SOAP vs. REST](https://blog.postman.com/soap-vs-rest/)
* [Introduction to GraphQL](https://graphql.org/learn/)
* [Comparing API Architectural Styles: SOAP vs REST vs GraphQL vs RPC](https://www.altexsoft.com/blog/soap-vs-rest-vs-graphql-vs-rpc/)

Even though GraphQL is on the rise and is being adopted by bigger and bigger companies, including GitHub and Shopify, the truth is that the majority of public APIs are still REST APIs. Therefore, for the purpose of this tutorial, you’ll learn only about REST APIs and how to consume them using Python.

### requests and APIs: A Match Made in Heaven

When consuming APIs with Python, there’s only one library you need: requests. With it, you should be able to do most, if not all, of the actions required to consume any public API.

You can install requests by running the following command in your console:

```python
$ python -m pip install requests
```

To follow the code examples in this tutorial, make sure you’re using Python 3.8.1 and requests 2.24.0 or higher.

## Calling Your First API Using Python

Enough talking—it’s time to make your first API call! For the first example, you’ll be calling a popular API for generating [random user data](https://randomuser.me/).

Throughout the tutorial, you’ll see new APIs introduced in alert blocks like the one below. It’s a convenient way for you to scroll through afterward and quickly spot all the new APIs you learned about.

> Random User Generator API: This is a great tool for [generating random user data](https://randomuser.me/). You can use it to generate any number of random users and associated data, and you can also specify gender, nationality, and many other filters that can be really helpful when testing apps or, in this case, APIs.

The only thing you need to start with the Random User Generator API is to know which URL to call it with. For this example, the URL to use is `https://randomuser.me/api/`, and this is the tiniest API call you can make:


```python
import requests
requests.get("https://randomuser.me/api/")
```




    <Response [200]>



<Response [200]>
In this small example, you import the requests library and then fetch (or get) data from the URL for the Random User Generator API. But you don’t actually see any of the data returned. What you get instead is a Response [200], which in API terms means everything went OK.

If you want to see the actual data, then you can use .text from the returned Response object:


```python
response = requests.get("https://randomuser.me/api/")
response.text
```




    '{"results":[{"gender":"male","name":{"title":"Mr","first":"Kadir","last":"Beşok"},"location":{"street":{"number":9409,"name":"Fatih Sultan Mehmet Cd"},"city":"Sivas","state":"Kırklareli","country":"Turkey","postcode":18240,"coordinates":{"latitude":"71.2646","longitude":"-30.1599"},"timezone":{"offset":"+2:00","description":"Kaliningrad, South Africa"}},"email":"kadir.besok@example.com","login":{"uuid":"738fcb71-91b0-4920-8ff5-61d3aea35a2d","username":"whitegoose493","password":"xerxes","salt":"MhTbKkbs","md5":"7bffca4a421eb11fef090a6f6eaf825a","sha1":"9aa85d20bb4c2b11e94b8d894faafdc511f234ee","sha256":"00830c682e40d5e6aac095b6ab86fbdda805eb0901428de88030b6d52e493535"},"dob":{"date":"1950-07-25T05:25:30.373Z","age":71},"registered":{"date":"2017-06-02T01:02:42.154Z","age":4},"phone":"(696)-136-1873","cell":"(645)-315-9173","id":{"name":"","value":null},"picture":{"large":"https://randomuser.me/api/portraits/men/22.jpg","medium":"https://randomuser.me/api/portraits/med/men/22.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/22.jpg"},"nat":"TR"}],"info":{"seed":"8dc6d2e919bd7b3d","results":1,"page":1,"version":"1.3"}}'



### Endpoints and Resources

As you saw above, the first thing you need to know for consuming an API is the API URL, typically called the base URL. The base URL structure is no different from the URLs you use for browsing Google, YouTube, or Facebook, though it usually contains the word api. This is not mandatory, just more of a rule of thumb.

For example, here are the base URLs for a few well-known API players:

* https://api.twitter.com
* https://api.github.com
* https://api.stripe.com

As you can see, all of the above start with https://api and include the remaining official domain, such as .twitter.com or .github.com. There’s no specific standard for how the API base URL should look, but it’s quite common for it to mimic this structure.

If you try opening any of the above links, then you’ll notice that most of them will return an error or ask for credentials. That’s because APIs sometimes require authentication steps before you can use them. You’ll learn more about this a bit later in the tutorial.

>TheDogAPI: This API is quite fun but also a really good example of a well-done API with great [documentation](https://thedogapi.com/). With it, you can fetch the different dog breeds and some images, but if you register, you can also cast votes on your favorite dogs.

Next, using the just-introduced [TheDogAPI](https://thedogapi.com/), you’ll try to make a basic request to see how it may differ from the Random User Generator API you tried above:


```python
response = requests.get("https://api.thedogapi.com/")
response.text
```




    '{"message":"The Dog API"}'



In this case, when calling the base URL, you get this generic message saying The Dog API. This is because you’re calling the base URL, which is typically used for very basic information about an API, not the real data.

Calling the base URL alone isn’t a lot of fun, but that’s where endpoints come in handy. An endpoint is a part of the URL that specifies what resource you want to fetch. Well-documented APIs usually contain an API reference, which is extremely useful for knowing the exact endpoints and resources an API has and how to use them.

You can check the [official documentation](https://docs.thedogapi.com/api-reference) to learn more about how to use TheDogAPI and what endpoints are available. In there, you’ll find a [/breeds](https://docs.thedogapi.com/api-reference/breeds/breeds-list) endpoint that you can use to fetch all the available breed resources or objects.

If you scroll down, then you’ll find the Send a Test Request section, where you’ll see a form for testing.

This is something that you’ll see in many API documentations: a way for you to quickly test the API directly from the documentation page. In this case, you can click Send to quickly get the result of calling that endpoint. Et voilà, you just called an API without having to write any code for it.

Now, give it a try in code locally using the [breeds](https://docs.thedogapi.com/api-reference/breeds/breeds-list) endpoint and some of the API knowledge you already have:


```python
response = requests.get("https://api.thedogapi.com/v1/breeds")
response.text[:200] # sliced for brevity
```




    '[{"weight":{"imperial":"6 - 13","metric":"3 - 6"},"height":{"imperial":"9 - 11.5","metric":"23 - 29"},"id":1,"name":"Affenpinscher","bred_for":"Small rodent hunting, lapdog","breed_group":"Toy","life_'



If you’re a cat person, don’t fret. There’s an API for you, too, with the same endpoint but a different base URL:


```python
response = requests.get("https://api.thecatapi.com/v1/breeds")
response.text[-200:]
```




    'en.wikipedia.org/wiki/York_Chocolate","hypoallergenic":0,"reference_image_id":"0SxW2SQ_S","image":{"id":"0SxW2SQ_S","width":800,"height":1203,"url":"https://cdn2.thecatapi.com/images/0SxW2SQ_S.jpg"}}]'



I bet you’re already thinking about different ways you can use these APIs to make some cute side project, and that’s the great thing about APIs. Once you start using them, there’s nothing stopping you from turning a hobby or passion into a fun little project.

Before you move forward, one thing you need to know about endpoints is the difference between `http://` and `https://`. In a nutshell, `HTTPS` is the encrypted version of `HTTP`, making all traffic between the client and the server much safer. When consuming public APIs, you should definitely stay away from sending any private or sensitive information to `http://` endpoints and use only those APIs that provide a secure `https://` base URL.

For more information on why it’s important to stick to HTTPS when online browsing, check out [Exploring HTTPS With Python](https://realpython.com/python-https/).

In the next section, you’ll dig a bit further into the main components of an API call.

### Request and Response

As you very briefly read above, all interactions between a client—in this case your 
Python console—and an API are split into a request and a response:

* **Requests** contain relevant data regarding your API request call, such as the base URL, the endpoint, the method used, the headers, and so on.
* **Responses** contain relevant data returned by the server, including the data or content, the status code, and the headers.

Using TheDogAPI again, you can drill down a bit more into what exactly is inside the Request and Response objects:


```python
response = requests.get("https://api.thedogapi.com/v1/breeds")
response
```




    <Response [200]>




```python
response.request
```




    <PreparedRequest [GET]>




```python
request = response.request
request.url
```




    'https://api.thedogapi.com/v1/breeds'




```python
request.path_url
```




    '/v1/breeds'




```python
request.method
```




    'GET'




```python
request.headers
```




    {'User-Agent': 'python-requests/2.26.0', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive'}




```python
response
```




    <Response [200]>




```python
response.text[:200]
```




    '[{"weight":{"imperial":"6 - 13","metric":"3 - 6"},"height":{"imperial":"9 - 11.5","metric":"23 - 29"},"id":1,"name":"Affenpinscher","bred_for":"Small rodent hunting, lapdog","breed_group":"Toy","life_'




```python
response.status_code
```




    200




```python
response.headers
```




    {'x-dns-prefetch-control': 'off', 'x-frame-options': 'SAMEORIGIN', 'strict-transport-security': 'max-age=15552000; includeSubDomains', 'x-download-options': 'noopen', 'x-content-type-options': 'nosniff', 'x-xss-protection': '1; mode=block', 'vary': 'Origin', 'pagination-count': '172', 'pagination-page': '0', 'pagination-limit': '1000', 'access-control-expose-headers': 'Pagination-Count, Pagination-Page, Pagination-Limit', 'content-type': 'application/json; charset=utf-8', 'x-response-time': '6ms', 'X-Cloud-Trace-Context': '5fd785f3cc96fd46716a688f232d7e20', 'Date': 'Wed, 01 Dec 2021 19:56:27 GMT', 'Server': 'Google Frontend', 'Content-Length': '76246'}



The example above shows you a few of the most important attributes available for Request and Response objects.

You’ll learn more about some of these attributes in this tutorial, but if you want to dig even further, then you can check Mozilla’s documentation on HTTP messages for a more in-depth explanation of each attribute.

### Status Codes

Status codes are one of the most important pieces of information to look for in any API response. They tell you if your request was successful, if it’s missing data, if it’s missing credentials, and so on.

With time, you’ll recognize the different status codes without help. But for now, here’s a list with some of the most common status codes you’ll find:

| Status code |	Description |
|:-- |:-- |
| 200 OK	| Your request was successful! |
| 201 Created	| Your request was accepted and the resource was created. |
| 400 Bad Request	| Your request is either wrong or missing some information. |
| 401 Unauthorized	| Your request requires some additional permissions. |
| 404 Not Found	| The requested resource does not exist. |
| 405 Method Not Allowed	| The endpoint does not allow for that specific HTTP method. |
| 500 Internal Server Error	| Your request wasn’t expected and probably broke something on the server side. |

You saw 200 OK earlier in the examples you executed, and you might even recognize 404 Not Found from browsing the web.

>Fun fact: Companies tend to use 404 error pages for private jokes or pure fun, like these examples below:
>* [Mantra Labs](https://www.mantralabsglobal.com/404)
>* [Gymbox](https://www.gymbox.com/404)
>* [Pixar](https://www.pixar.com/404)
>* [Slack](https://slack.com/404)
>
>In the API world, though, developers have limited space in the response for this kind of fun. But they make up for it in other places, like the HTTP headers. You’ll see some examples soon enough!

You can check the status of a response using `.status_code` and `.reason`. The requests library also prints the status code in the representation of the Response object:


```python
response = requests.get("https://api.thedogapi.com/v1/breeds")
response
```




    <Response [200]>




```python
response.status_code
```




    200




```python
response.reason
```




    'OK'



The request above returns 200, so you can consider it a successful request. But now have a look at a failing request triggered when you include a typo in the endpoint /breedz:


```python
response = requests.get("https://api.thedogapi.com/v1/breedz")
response
```




    <Response [404]>




```python
response.status_code
```




    404




```python
response.reason
```




    'Not Found'



As you can see, the /breedz endpoint doesn’t exist, so the API returns a 404 Not Found status code.

You can use these status codes to quickly see if your request needs to be changed or if you should check the documentation again for any typos or missing pieces.

### HTTP Headers

HTTP headers are used to define a few parameters governing requests and responses:

| HTTP Header | Description |
| :-- | :-- |
| Accept | What type of content the client can accept |
| Content-Type | What type of content the server will respond with |
| User-Agent | What software the client is using to communicate with the server |
| Server | What software the server is using to communicate with the client |
| Authentication | Who is calling the API and what credentials they have |

There are many other headers that you can find when inspecting a request or response. Have a look at [Mozilla’s extended list](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) if you’re curious about the specific use for each of them.

To inspect the headers of a response, you can use `response.headers`:


```python
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
response.headers
```




    {'x-dns-prefetch-control': 'off', 'x-frame-options': 'SAMEORIGIN', 'strict-transport-security': 'max-age=15552000; includeSubDomains', 'x-download-options': 'noopen', 'x-content-type-options': 'nosniff', 'x-xss-protection': '1; mode=block', 'vary': 'Origin', 'content-type': 'application/json; charset=utf-8', 'x-response-time': '1ms', 'X-Cloud-Trace-Context': '25ec7d4a8039178e30fa1df7c0b3cb89', 'Date': 'Wed, 01 Dec 2021 20:09:19 GMT', 'Server': 'Google Frontend', 'Content-Length': '357'}



To do the same with the request headers, you can use response.request.headers since request is an attribute of the Response object:


```python
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
response.request.headers
```




    {'User-Agent': 'python-requests/2.26.0', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive'}



In this case, you don’t define any specific headers when you make the request, so the default headers are returned.

### Custom Headers

Another standard that you might come across when consuming APIs is the use of custom headers. These usually start with X-, but they’re not required to. API developers typically use custom headers to send or request additional custom information from clients.

> Fun fact: A few companies go to extra lengths to be funny and innovative, using HTTP headers in a way they [weren’t meant to be used](https://frenxi.com/http-headers-you-dont-expect/), such as to solicit job applications.

You can use a dictionary to define headers, and you can send them along with your request using the headers parameter of `.get()`.

For example, say you want to send some request ID to the API server, and you know you can do that using `X-Request-Id`:


```python
headers = {"X-Request-Id": "<my-request-id>"}
response = requests.get("https://example.org", headers=headers)
response.request.headers
```




    {'User-Agent': 'python-requests/2.26.0', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive', 'X-Request-Id': '<my-request-id>'}



If you go through the `request.headers` dictionary, then you’ll find `X-Request-Id` right at the end, among a few other headers that come by default with any API request.

There are many useful headers a response might have, but one of the most important ones is Content-Type, which defines the kind of content returned in the response.

### Content-Type

These days, most APIs use [JSON](https://realpython.com/python-json/) as the default content type, but you might need to use an API that returns XML or other media types, such as images or video. In that case, the content type will differ.

If you look back to one of the previous examples using TheDogAPI and try to inspect the Content-Type header, then you’ll notice how it was defined as `application/json`:


```python
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
response.headers.get("Content-Type")
```




    'application/json; charset=utf-8'



Apart from the specific type of content (in this case application/json), the header might also return the specified encoding for the response content.

If, for example, you try to fetch an image of a goat from the following API, then you’ll notice that the content type is no longer application/json, but instead it’s defined as image/jpeg:


```python
response = requests.get("https://picsum.photos/200/300")
response
```




    <Response [200]>




```python
response.headers.get("Content-Type")
```




    'image/jpeg'



In this case, the Content-Type header states that the returned content is a JPEG image. You’ll learn how to view this content in the next section.

The `Content-Type` header is very important for you to know how to handle a response and what to do with its content. There are [hundreds](http://www.iana.org/assignments/media-types/media-types.xhtml) of other acceptable content types, including audio, video, fonts, and more.

### Response Content

As you just learned, the type of content you find in the API response will vary according to the Content-Type header. To properly read the response contents according to the different Content-Type headers, the requests package comes with a couple of different Response attributes you can use to manipulate the response data:

* **.text** returns the response contents in Unicode format.
* **.content** returns the response contents in bytes.

You already used the `.text` attribute above. But for some specific types of data, like images and other nontextual data, using `.content` is typically a better approach, even if it returns a very similar result to `.text`:


```python
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
response.headers.get("Content-Type")
```




    'application/json; charset=utf-8'




```python
response.content
```




    b'{"weight":{"imperial":"6 - 13","metric":"3 - 6"},"height":{"imperial":"9 - 11.5","metric":"23 - 29"},"id":1,"name":"Affenpinscher","bred_for":"Small rodent hunting, lapdog","breed_group":"Toy","life_span":"10 - 12 years","temperament":"Stubborn, Curious, Playful, Adventurous, Active, Fun-loving","origin":"Germany, France","reference_image_id":"BJa4kxc4X"}'



As you can see, there isn’t a big difference between `.content` and the previously used `.text`.

However, by looking at the response’s `Content-Type` header, you can see the content is `application/json;`, a `JSON` object. For that kind of content, the requests library includes a specific `.json()` method that you can use to immediately convert the API bytes response into a Python data structure:


```python
response = requests.get("https://api.thedogapi.com/v1/breeds/1")
response.headers.get("Content-Type")
```




    'application/json; charset=utf-8'




```python
response.json()
```




    {'weight': {'imperial': '6 - 13', 'metric': '3 - 6'},
     'height': {'imperial': '9 - 11.5', 'metric': '23 - 29'},
     'id': 1,
     'name': 'Affenpinscher',
     'bred_for': 'Small rodent hunting, lapdog',
     'breed_group': 'Toy',
     'life_span': '10 - 12 years',
     'temperament': 'Stubborn, Curious, Playful, Adventurous, Active, Fun-loving',
     'origin': 'Germany, France',
     'reference_image_id': 'BJa4kxc4X'}




```python
response.json()["name"]
```




    'Affenpinscher'



As you can see, after executing `response.json()`, you get a dictionary that you’re able to use as you’d use any other dictionary in Python.

Now, looking back at the recent example you ran using the image API, try to fetch that same image and have a look at its content:


```python
response = requests.get("https://picsum.photos/200/300")
response
```




    <Response [200]>




```python
response.headers.get("Content-Type")
```




    'image/jpeg'




```python
response.content[:200]
```




    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xe1\x00\xdeExif\x00\x00II*\x00\x08\x00\x00\x00\x06\x00\x12\x01\x03\x00\x01\x00\x00\x00\x01\x00\x00\x00\x1a\x01\x05\x00\x01\x00\x00\x00V\x00\x00\x00\x1b\x01\x05\x00\x01\x00\x00\x00^\x00\x00\x00(\x01\x03\x00\x01\x00\x00\x00\x02\x00\x00\x00\x13\x02\x03\x00\x01\x00\x00\x00\x01\x00\x00\x00i\x87\x04\x00\x01\x00\x00\x00f\x00\x00\x00\x00\x00\x00\x008c\x00\x00\xe8\x03\x00\x008c\x00\x00\xe8\x03\x00\x00\x07\x00\x00\x90\x07\x00\x04\x00\x00\x000210\x01\x91\x07\x00\x04\x00\x00\x00\x01\x02\x03\x00\x86\x92\x07\x00\x16\x00\x00\x00\xc0\x00\x00\x00\x00\xa0\x07\x00\x04\x00\x00\x000100\x01\xa0\x03\x00\x01\x00\x00\x00\xff\xff\x00\x00\x02\xa0\x04\x00\x01\x00'



In this case, because you’re requesting an image, .content isn’t very helpful. In fact, it’s nearly impossible to understand. However, you know this is a JPEG image, so you can try storing it into a file and see what happens:


```python
response = requests.get("https://picsum.photos/200/300")
file = open("placeholder.jpeg", "wb")
file.write(response.content)
file.close()
```

Now if you open the folder you’re working from, then you’ll find a `placeholder.jpeg' file, which is a random image that you just fetched using an API. Isn’t that amazing?
![placeholder](placeholder.jpeg)

### HTTP Methods

When calling an API, there are a few different methods, also called verbs, that you can use to specify what action you want to execute. For example, if you wanted to fetch some data, you’d use the method GET, and if you wanted to create some data, then you’d use the method POST.

When purely consuming data using APIs, you’ll typically stick to GET requests, but here’s a list of the most common methods and their typical use case:

| HTTP Method | Description | Requests method |
| :-- | :-- | :-- |
| POST | Create a new resource. | `requests.post()` |
| GET | Read an existing resource. | `requests.get()` |
| PUT | Update an existing resource. | `requests.put()` |
| DELETE | Delete an existing resource. | `requests.delete()` |

These four methods are typically referred to as CRUD operations as they allow you to create, read, update and delete resources.

> Note: There’s an additional `PATCH` method that’s also associated with CRUD operations, but it’s slightly less common than the four above. It’s used to make partial modifications instead of completely replacing a resource using `PUT`.
>
> You can read a bit more about the [differences between PUT and PATCH](https://medium.com/backticks-tildes/restful-api-design-put-vs-patch-4a061aa3ed0b) to understand their different needs.

If you’re curious about the remaining HTTP methods, or if you just want to learn a bit more about those already mentioned, then have a look through [Mozilla’s documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

Until now, you’ve only used `.get()` to fetch data, but you can use the requests package for all the other HTTP methods as well:


```python
requests.post("https://api.thedogapi.com/v1/breeds/1")
```




    <Response [405]>




```python
requests.get("https://api.thedogapi.com/v1/breeds/1")
```




    <Response [200]>




```python
requests.put("https://api.thedogapi.com/v1/breeds/1")
```




    <Response [405]>




```python
requests.delete("https://api.thedogapi.com/v1/breeds/1")
```




    <Response [405]>



If you try these on your console, then you’ll notice that most of them will return a 405 Method Not Allowed [status code](https://realpython.com/python-api/#status-codes). That’s because not all endpoints will allow for `POST`, `PUT`, or `DELETE` methods. Especially when you’re reading data using public APIs, you’ll find that most APIs will only allow `GET` requests since you’re not allowed to create or change the existing data.

### Query Parameters

Sometimes when you call an API, you get a ton of data that you don’t need or want. For example, when calling TheDogAPI’s `/breeds` endpoint, you get a lot of information about a given breed. But in some cases, you might want to extract only certain information about a given breed. That’s where query parameters come in!

You might have seen or used query parameters when browsing online. For example when watching a YouTube video, you have a URL like https://www.youtube.com/watch?v=aL5GK2LVMWI. The `v=` in the URL is what you call a query parameter. It typically comes after the base URL and endpoint.

To add a query parameter to a given URL, you have to add a question mark (`?`) before the first query parameter. If you want to have multiple query parameters in your request, then you can split them with an ampersand (`&`).

The same YouTube URL above with multiple query parameters would look like this: https://www.youtube.com/watch?v=aL5GK2LVMWI&t=75.

In the API world, query parameters are used as filters you can send with your API request to further narrow down the responses. For example, going back to the Random User Generator API, you know how to generate a random user:


```python
requests.get("https://randomuser.me/api/").json()
```




    {'results': [{'gender': 'female',
       'name': {'title': 'Ms', 'first': 'Rose', 'last': 'Holland'},
       'location': {'street': {'number': 5926, 'name': 'Lone Wolf Trail'},
        'city': 'Charlotte',
        'state': 'Montana',
        'country': 'United States',
        'postcode': 31757,
        'coordinates': {'latitude': '80.8707', 'longitude': '164.4143'},
        'timezone': {'offset': '+4:00',
         'description': 'Abu Dhabi, Muscat, Baku, Tbilisi'}},
       'email': 'rose.holland@example.com',
       'login': {'uuid': 'd6e99728-3532-40c3-a0e5-ab883ae2bb1c',
        'username': 'greenostrich727',
        'password': 'titts',
        'salt': 'wnhaXpka',
        'md5': '62476aa7e4d48627819a60c9e0d78848',
        'sha1': '9989fd950fa1b0ab989b26a63283eae06e8c48fb',
        'sha256': '20e8792b196ca4b5a2862f74a930fa04d5b0b7963f72d472fc9944eec9147efe'},
       'dob': {'date': '1973-04-02T22:04:06.954Z', 'age': 48},
       'registered': {'date': '2011-11-24T23:14:03.932Z', 'age': 10},
       'phone': '(691)-760-7310',
       'cell': '(966)-817-2820',
       'id': {'name': 'SSN', 'value': '571-02-2197'},
       'picture': {'large': 'https://randomuser.me/api/portraits/women/23.jpg',
        'medium': 'https://randomuser.me/api/portraits/med/women/23.jpg',
        'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/23.jpg'},
       'nat': 'US'}],
     'info': {'seed': 'c4c34c4f9e349852',
      'results': 1,
      'page': 1,
      'version': '1.3'}}



However, let’s say you specifically want to generate only random female users. According to the documentation, you can use the query parameter gender= for that:


```python
requests.get("https://randomuser.me/api/?gender=female").json()
```




    {'results': [{'gender': 'female',
       'name': {'title': 'Ms', 'first': 'Iina', 'last': 'Lampinen'},
       'location': {'street': {'number': 9488, 'name': 'Suvantokatu'},
        'city': 'Isokyrö',
        'state': 'Central Ostrobothnia',
        'country': 'Finland',
        'postcode': 74680,
        'coordinates': {'latitude': '-14.8635', 'longitude': '-57.0888'},
        'timezone': {'offset': '+9:30', 'description': 'Adelaide, Darwin'}},
       'email': 'iina.lampinen@example.com',
       'login': {'uuid': '7eefd21b-180d-4090-ae73-f9c6bacfa363',
        'username': 'heavyduck989',
        'password': 'tank',
        'salt': 'fHbYbLcz',
        'md5': 'f12032c643eb76d532046b631f5ae87e',
        'sha1': 'df5a6b65dc99c3d1e9cbe503cca1c9800be711b8',
        'sha256': 'ce264c3d8015f65307d370347a9d6b29c5567d9a04bfef30e8824a4833c2fc45'},
       'dob': {'date': '1975-03-01T03:20:24.611Z', 'age': 46},
       'registered': {'date': '2016-02-07T22:42:12.742Z', 'age': 5},
       'phone': '07-679-624',
       'cell': '041-764-69-11',
       'id': {'name': 'HETU', 'value': 'NaNNA340undefined'},
       'picture': {'large': 'https://randomuser.me/api/portraits/women/38.jpg',
        'medium': 'https://randomuser.me/api/portraits/med/women/38.jpg',
        'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/38.jpg'},
       'nat': 'FI'}],
     'info': {'seed': 'c2d5fba97f0073e9',
      'results': 1,
      'page': 1,
      'version': '1.3'}}



That’s great! Now let’s say you want to generate only female users from Germany. Again, looking through the documentation, you find a section on nationality, and you can use the query parameter `nat=` for that:


```python
requests.get("https://randomuser.me/api/?gender=female&nat=de").json()
```




    {'results': [{'gender': 'female',
       'name': {'title': 'Mrs', 'first': 'Tina', 'last': 'Kohnen'},
       'location': {'street': {'number': 6295, 'name': 'Waldstraße'},
        'city': 'Franzburg',
        'state': 'Sachsen-Anhalt',
        'country': 'Germany',
        'postcode': 74858,
        'coordinates': {'latitude': '5.5969', 'longitude': '155.0415'},
        'timezone': {'offset': '+7:00', 'description': 'Bangkok, Hanoi, Jakarta'}},
       'email': 'tina.kohnen@example.com',
       'login': {'uuid': '79caf4db-602a-413b-aa01-11f13caabbca',
        'username': 'angrybutterfly162',
        'password': 'oooooo',
        'salt': 'xdjQgmSO',
        'md5': 'df0022b87ac5223578e0585ee6ad4dea',
        'sha1': '47d9e4c151f934ab95db1a7d1403fa0dcafe3b25',
        'sha256': '4892bc1ec6f3cd3c4bb650c6921eaa481f793d7b305de1593b20564f4a81a7be'},
       'dob': {'date': '1950-06-09T17:03:05.683Z', 'age': 71},
       'registered': {'date': '2019-01-03T21:13:16.208Z', 'age': 2},
       'phone': '0276-6777692',
       'cell': '0177-3641373',
       'id': {'name': '', 'value': None},
       'picture': {'large': 'https://randomuser.me/api/portraits/women/9.jpg',
        'medium': 'https://randomuser.me/api/portraits/med/women/9.jpg',
        'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/9.jpg'},
       'nat': 'DE'}],
     'info': {'seed': 'bda46856652ee73e',
      'results': 1,
      'page': 1,
      'version': '1.3'}}



Using query parameters, you can start fetching more specific data from an API, making the whole experience a bit more tailored to your needs.

To avoid having to rebuild the URL over and over again, you can use the params attribute to send in a dictionary of all query parameters to append to a URL:


```python
query_params = {"gender": "female", "nat": "de"}
requests.get("https://randomuser.me/api/", params=query_params).json()
```




    {'results': [{'gender': 'female',
       'name': {'title': 'Miss', 'first': 'Auguste', 'last': 'Schümann'},
       'location': {'street': {'number': 1899, 'name': 'Meisenweg'},
        'city': 'Xanten',
        'state': 'Bremen',
        'country': 'Germany',
        'postcode': 61351,
        'coordinates': {'latitude': '5.5967', 'longitude': '-142.9741'},
        'timezone': {'offset': '+9:30', 'description': 'Adelaide, Darwin'}},
       'email': 'auguste.schumann@example.com',
       'login': {'uuid': 'd2e3af49-c87e-42f3-9270-2886cb237037',
        'username': 'heavybird261',
        'password': 'bowwow',
        'salt': 'WHE4h7nw',
        'md5': 'fd513c683a4e82b3ea4b7d506b165925',
        'sha1': '70958c393f4f530782bf4e45f354ff3d19805ca6',
        'sha256': '05e04247fd9e5869d9d548d049eedd2b62d538c962cc65a2f6f473c52dc8138b'},
       'dob': {'date': '1973-12-02T15:39:25.306Z', 'age': 48},
       'registered': {'date': '2011-07-28T07:37:36.226Z', 'age': 10},
       'phone': '0861-2402473',
       'cell': '0172-8346935',
       'id': {'name': '', 'value': None},
       'picture': {'large': 'https://randomuser.me/api/portraits/women/41.jpg',
        'medium': 'https://randomuser.me/api/portraits/med/women/41.jpg',
        'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/41.jpg'},
       'nat': 'DE'}],
     'info': {'seed': '868424ecf72bfc5b',
      'results': 1,
      'page': 1,
      'version': '1.3'}}



You can apply the above to any other API you like. If you go back to TheDogAPI, the documentation has a way for you to filter the breeds endpoint to return only the breeds that match a specific name. For example, if you wanted to look for the Labradoodle breed, then you could do that with the query parameter `q`:


```python
query_params = {"q": "labradoodle"}
endpoint = "https://api.thedogapi.com/v1/breeds/search"
requests.get(endpoint, params=query_params).json()
```




    [{'weight': {'imperial': '45 - 100', 'metric': '20 - 45'},
      'height': {'imperial': '14 - 24', 'metric': '36 - 61'},
      'id': 148,
      'name': 'Labradoodle',
      'breed_group': 'Mixed',
      'life_span': '10 - 15 years'}]



There you have it! By sending the query parameter `q` with the value labradoodle, you’re able to filter all breeds that match that specific value.

> Tip: When you’re reusing the same endpoint, it’s a best practice to define it as a [variable](https://realpython.com/python-variables/) at the top of your code. This will make your life easier when interacting with an API over and over again.

With the help of query parameters, you’re able to further narrow your requests and specify exactly what you’re looking for. Most APIs you’ll find online will have some sort of query parameters that you can use to filter data. Remember to look through the documentation and API reference to find them.

## Learning Advanced API Concepts

Now that you have a good understanding of the basics of API consumption using Python, there are a few more advanced topics that are worth touching upon, even if briefly, such as [authentication](https://realpython.com/python-api/#authentication), [pagination](https://realpython.com/python-api/#pagination), and [rate limiting](https://realpython.com/python-api/#rate-limiting).

### Authentication

API authentication is perhaps the most complex topic covered in this tutorial. Even though a lot of public APIs are free and completely public, an even bigger number of APIs are available behind some form of authentication. There are numerous APIs that require authentication, but here are a few good examples:

* [GitHub API](https://docs.github.com/en/free-pro-team@latest/rest)
* [Twitter API](https://developer.twitter.com/en/docs)
* [Instagram API](https://developers.facebook.com/docs/instagram-basic-display-api)

Authentication approaches range from the simplistic and straightforward, like those using API keys or Basic Authentication, to much more complex and safer techniques, like OAuth.

Typically, calling an API without credentials or with the wrong ones will return a 401 Unauthorized or 403 Forbidden status code.

### API Keys

The most common level of authentication is the API key. These keys are used to identify you as an API user or customer and to trace your use of the API. API keys are typically sent as a request header or as a query parameter.

> NASA APIs: One of the coolest collections of publicly available APIs is the one provided by [NASA](https://api.nasa.gov/). You can find APIs to fetch the [astronomy picture of the day](https://apod.nasa.gov/apod/astropix.html) or pictures taken by the [Earth Polychromatic Imaging Camera (EPIC)](https://epic.gsfc.nasa.gov/), among others.

For this example, you’ll have a go at NASA’s [Mars Rover Photo API](https://github.com/chrisccerami/mars-photo-api), and you’ll fetch pictures taken on July 1, 2020. For testing purposes, you can use the DEMO_KEY API key that NASA provides by default. Otherwise, you can quickly generate your own by going to NASA’s [main API page](https://api.nasa.gov/) and clicking Get Started.

You can add the API key to your request by appending the api_key= query parameter:


```python
from dotenv import dotenv_values
config = dotenv_values("nasa.env")

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

query_params = {"api_key": config['API_KEY'], "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)
response
```




    <Response [200]>



So far, so good. You managed to make an authenticated request to NASA’s API and to get back a 200 OK response.

Now have a look at the Response object and try to extract some pictures from it:


```python
response.json()
```




    {'photos': [{'id': 754118,
       'sol': 2809,
       'camera': {'id': 20,
        'name': 'FHAZ',
        'rover_id': 5,
        'full_name': 'Front Hazard Avoidance Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/fcam/FLB_646868981EDR_F0810628FHAZ00337M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754119,
       'sol': 2809,
       'camera': {'id': 20,
        'name': 'FHAZ',
        'rover_id': 5,
        'full_name': 'Front Hazard Avoidance Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/fcam/FRB_646868981EDR_F0810628FHAZ00337M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754120,
       'sol': 2809,
       'camera': {'id': 20,
        'name': 'FHAZ',
        'rover_id': 5,
        'full_name': 'Front Hazard Avoidance Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/fcam/FRB_646860144EDR_F0810628FHAZ00337M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754121,
       'sol': 2809,
       'camera': {'id': 20,
        'name': 'FHAZ',
        'rover_id': 5,
        'full_name': 'Front Hazard Avoidance Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/fcam/FLB_646860144EDR_F0810628FHAZ00337M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754122,
       'sol': 2809,
       'camera': {'id': 21,
        'name': 'RHAZ',
        'rover_id': 5,
        'full_name': 'Rear Hazard Avoidance Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/rcam/RRB_646869036EDR_F0810628RHAZ00337M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754123,
       'sol': 2809,
       'camera': {'id': 21,
        'name': 'RHAZ',
        'rover_id': 5,
        'full_name': 'Rear Hazard Avoidance Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/rcam/RLB_646869036EDR_F0810628RHAZ00337M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754124,
       'sol': 2809,
       'camera': {'id': 21,
        'name': 'RHAZ',
        'rover_id': 5,
        'full_name': 'Rear Hazard Avoidance Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/rcam/RRB_646860185EDR_F0810628RHAZ00337M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754125,
       'sol': 2809,
       'camera': {'id': 21,
        'name': 'RHAZ',
        'rover_id': 5,
        'full_name': 'Rear Hazard Avoidance Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/rcam/RLB_646860185EDR_F0810628RHAZ00337M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754126,
       'sol': 2809,
       'camera': {'id': 26,
        'name': 'NAVCAM',
        'rover_id': 5,
        'full_name': 'Navigation Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/ncam/NLB_646869070EDR_F0810628NCAM00229M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754127,
       'sol': 2809,
       'camera': {'id': 26,
        'name': 'NAVCAM',
        'rover_id': 5,
        'full_name': 'Navigation Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/ncam/NLB_646860211EDR_F0810628NCAM00229M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754128,
       'sol': 2809,
       'camera': {'id': 26,
        'name': 'NAVCAM',
        'rover_id': 5,
        'full_name': 'Navigation Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/ncam/NRB_646869070EDR_F0810628NCAM00229M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}},
      {'id': 754129,
       'sol': 2809,
       'camera': {'id': 26,
        'name': 'NAVCAM',
        'rover_id': 5,
        'full_name': 'Navigation Camera'},
       'img_src': 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/ncam/NRB_646860211EDR_F0810628NCAM00229M_.JPG',
       'earth_date': '2020-07-01',
       'rover': {'id': 5,
        'name': 'Curiosity',
        'landing_date': '2012-08-06',
        'launch_date': '2011-11-26',
        'status': 'active'}}]}




```python
photos = response.json()["photos"]
```


```python
print(f"Found {len(photos)} photos")
```

    Found 12 photos



```python
photos[4]["img_src"]
```




    'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/rcam/RRB_646869036EDR_F0810628RHAZ00337M_.JPG'



Using `.json()` to convert the response to a Python dictionary and then fetching the photos field from the response, you’re able to iterate through all Photo objects and even fetch a specific photo’s image URL. If you open that URL in your browser, then you’ll see the following picture of Mars taken by one of the Mars rovers

For this example, you picked a specific earth_date (2020-07-01) and then a specific photo from the response dictionary (4). Before moving forward, try changing the date or fetching pictures from a different [camera](https://github.com/chrisccerami/mars-photo-api#cameras) to see how it changes the end result.

### OAuth: Getting Started

Another very common standard in API authentication is [OAuth](https://oauth.net/). You’ll learn only the essentials of OAuth in this tutorial since it’s a very broad topic.

Even if you weren’t aware that it was part of OAuth, you may have seen and used the OAuth flow multiple times. Every time an app or platform has a Login With or Continue With option, that’s the starting point of an OAuth flow:

Here’s a step-by-step breakdown of what will happen if you click Continue With Facebook:

1. The Spotify app will ask the Facebook API to start an authentication flow. To do this, the Spotify app will send its application ID (client_id) and a URL (redirect_uri) to redirect the user after success or error.
2. You’ll be redirected to the Facebook website and asked to log in with your credentials. The Spotify app won’t see or have access to these credentials. This is the most important benefit of OAuth.
3. Facebook will show you all the data the Spotify app is requesting from your profile and ask you to accept or reject sharing that data.
4. If you accept giving Spotify access to your data, then you’ll be redirected back to the Spotify app, already logged in.

When going through step 4, Facebook will provide Spotify with a special credential (access_token) that can be used repeatedly to fetch your information. This specific Facebook login token is valid for sixty days, but other apps might have different expiration periods. If you’re curious, then Facebook has a [settings page](https://www.facebook.com/settings?tab=applications&ref=settings) that you can check to see which apps have been given your Facebook access token.

Now, from a more technical standpoint, here are the things you need to know when consuming APIs using OAuth:

* You need to create an application that will have an ID (`app_id` or `client_id`) and a secret (`app_secret` or `client_secret`).
* You need to have a redirect URL (`redirect_uri`), which the API will use to send information to you.
* You’ll get a code as the result of the authentication, which you need to exchange for an access token.

There are a few variations to the above, but generally speaking, most OAuth flows will have steps similar to these.

> Tip: When you’re just testing things out and you need some sort of redirect URL to get a code, you can use a service called [httpbin](https://httpbin.org/).
>
>More specifically, you can use https://httpbin.org/anything as a redirect URL, as it’ll simply output whatever it gets as an input. You can test it yourself by navigating to that URL.

Next, you’ll dive into an example using the GitHub API!

### OAuth: A Practical Example

As you saw above, the first thing you need to do is create an application. There’s a great step-by-step explanation on how to do this in the [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/developers/apps/creating-an-oauth-app) that you can follow. The only thing to keep in mind is to use the https://httpbin.org/anything URL mentioned above for the Authorization callback URL field.

> GitHub API: You can use the [GitHub API](https://docs.github.com/en/rest) for a lot of different use cases, such as getting a list of repositories you’re a part of, getting a list of followers you have, and much more.

Once you’ve created your app, copy and paste the Client_ID and Client_Secret, together with your selected redirect URL, into a Python file called github.py:


```python
import requests
from dotenv import dotenv_values
config = dotenv_values("github.env")

# REPLACE the following variables with your Client ID and Client Secret
CLIENT_ID = config['CLIENT_ID']
CLIENT_SECRET = config['CLIENT_SECRET']

# REPLACE the following variable with what you added in the
# "Authorization callback URL" field
REDIRECT_URI = "https://httpbin.org/anything"
```

Now that you have all the important variables in place, you need to be able to create a link to redirect the user to their GitHub account, as explained in the GitHub documentation:


```python
def create_oauth_link():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user",
        "response_type": "code",
    }

    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params=params)
    url = response.url
    return url
```

In this piece of code, you first define the required parameters that the API expects and then call the API using the requests package and `.get()`.

When you make the request to the `/login/oauth/authorize` endpoint, the API will automatically redirect you to the GitHub website. In that case, you want to fetch the url parameter from the response. This parameter contains the exact URL that GitHub is redirecting you to.

The next step in the authorization flow is to exchange the code you get for an access token. Again, following the steps in GitHub’s documentation, you can make a method for it:


```python
def exchange_code_for_access_token(code=None):
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }

    headers = {"Accept": "application/json"}
    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, params=params, headers=headers).json()
    return response["access_token"]
```

Here, you make a `POST` request to exchange the code for an access token. In this request, you have to send your `CLIENT_SECRET` and code so that GitHub can validate that this specific code was initially generated by your application. Only then will the GitHub API generate a valid access token and return it to you.

Now you can add the following to your file and try running it:


```python
link = create_oauth_link()
print(f"Follow the link to start the authentication with GitHub: {link}")
code = input("GitHub code: ")
access_token = exchange_code_for_access_token(code)
print(f"Exchanged code {code} with access token: {access_token}")
```

If everything goes according to plan, then you should be rewarded with a valid access token that you can use to make calls to the GitHub API, impersonating the authenticated user.

Now try adding the following code to fetch your user profile using the User API and to print your name, username, and number of private repositories:


```python
def print_user_info(access_token=None):
    headers = {"Authorization": f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers).json()
    name = response["name"]
    username = response["login"]
    private_repos_count = response["total_private_repos"]
    print(
        f"{name} ({username}) | private repositories: {private_repos_count}"
    )
```

Now that you have a valid access token, you need to send it on all your API requests using the Authorization header. The response to your request will be a Python dictionary containing all the user information. From that dictionary, you want to fetch the fields name, login, and total_private_repos. You can also print the response variable to see what other fields are available.

Alright, that should be it! The only thing left to do is to put it all together and try it out:


```python
print_user_info(access_token=access_token)
```

    Brian J Kolowitz (BrianKolowitz) | private repositories: 3


Here’s what happens when you run the code above:

1. A link is generated asking you to go to a GitHub page for authentication.
2. After following that link and logging in with your GitHub credentials, you’re redirected to your defined callback URL with a code field in the query parameters: 
3. After pasting that code in your console, you exchange the code for a reusable access token.
4. Your user information is fetched using that access token. Your name, username, and private repositories count are printed.
If you follow the steps above, then you should get a similar end result to this one:

```bash
$ John Doe (johndoe) | number of private repositories: 42
```

There are quite a few steps to take here, but it’s important that you take the time to really understand each one. Most APIs using OAuth will share a lot of the same behavior, so knowing this process well will unlock a lot of potential when you’re reading data from APIs.

Feel free to improve this example and add more functionality, such as getting your public and starred repositories or iterating through your followers to identify the most popular ones.

There are plenty of great resources online about OAuth, and if consuming APIs behind OAuth is what you really need, then I’d advise you to do a bit more research on that topic specifically. Here are a few good places to start:

* [What the Heck is OAuth](https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth)?
* [OAuth 2 Simplified](https://aaronparecki.com/oauth-2-simplified/)
* [OAuth 2.0 Authorization Framework](https://auth0.com/docs/protocols/oauth2)

From an API consumption perspective, knowing OAuth will definitely come very in handy when you’re interacting with public APIs. Most APIs have adopted OAuth as their authentication standard, and with good reason.

### Pagination

Sending lots of data back and forth between clients and servers comes with a price: bandwidth. To make sure that servers can cope with a lot of requests, APIs typically use pagination.

In very simple terms, pagination is the act of splitting large amounts of data into multiple smaller pieces.

You probably recognize this from many other websites, and the concept is mostly the same across different sites. For APIs in specific, this is normally handled with the help of query parameters, mainly the following two:

1. A page attribute that defines which page you’re currently requesting
2. A size attribute that defines the size of each page

The specific query parameter names might vary a lot depending on the API developers, but the concept is the same. A few API players might also use HTTP headers or the JSON response to return current pagination filters in place.

Using the GitHub API again, you can find an events endpoint in the documentation that contains pagination query parameters. The parameter `per_page=` defines the number of items to return, and `page=` allows you to paginate through multiple results. Here’s how to use these parameters:


```python
response = requests.get("https://api.github.com/events?per_page=1&page=0")
response.json()[0]["id"]
```




    '19159189189'




```python
response = requests.get("https://api.github.com/events?per_page=1&page=1")
response.json()[0]["id"]
```




    '19159192226'




```python
response = requests.get("https://api.github.com/events?per_page=1&page=2")
response.json()[0]["id"]
```




    '19159198801'



With the first URL, you’re only able to fetch one event. But using the page= query parameter, you can keep paginating through results, making sure that you’re able to fetch all of the events without overloading the API.

### Rate Limiting

Given that APIs are public facing and can be used by anyone, people with bad intentions often try to abuse them. To prevent such attacks, you can use a technique called rate limiting, which restricts the number of requests that users can make in a given time frame.

Some APIs may actually block your IP or API keys if you go over the defined rate limit too often. Be careful not to exceed the limits set by the API developers. Otherwise, you might have to wait a while before calling that API again.

For the example below, you’ll once again use the GitHub API and the /events endpoint. According to its documentation, GitHub allows about sixty unauthenticated requests per hour. If you go above that, then you’ll get a 403 status code and won’t be able to make any more API calls for quite some time.

> Warning: Running the next piece of code will really block you from calling GitHub for some time, so make sure you don’t need access to GitHub’s API for a bit before you run it.

For the sake of demonstration, you’ll purposefully try to exceed GitHub’s rate limit to see what happens. In the code below, you’ll request data until you get a status code other than `200 OK`:


```python
endpoint = "https://api.github.com/events"
for i in range(100):
    response = requests.get(endpoint)
    if i % 10 == 0 or response.status_code != 200:
        print(f"{i} - {response.status_code}")
    if response.status_code != 200:
        break
```

    0 - 403


0 - 200
1 - 200
2 - 200
3 - 200
4 - 200
5 - 200
...
55 - 200
56 - 200
57 - 403


```python
response
```




    <Response [403]>




```python
response.json()
```




    {'message': "API rate limit exceeded for 72.95.128.204. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)",
     'documentation_url': 'https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting'}



There you have it: After about sixty requests, the API stopped returning `200 OK` responses and returned a `403 Forbidden` response instead, informing you that you exceeded the API rate limit.

Some APIs, like GitHub’s, might even include additional information in the headers regarding your current rate limit and how many requests you have remaining. These are very helpful for you to avoid going over the defined limit. Have a look at the latest response.headers to see if you can find those specific rate limiting headers.

## Consuming APIs With Python: Practical Examples

Now that you know all the theory and have experimented with a few APIs, you can consolidate those learnings with some more practical examples. You can modify the examples below to tailor them to your own purposes.

### Searching and Fetching Trending GIFs

How about making a small script that fetches the top three trending GIFs from the [GIPHY](https://giphy.com/) website? To do this, you need to create an app and get an API key from GIPHY. You can find instructions by expanding the box below, and you can also check GIPHY’s [quickstart documentation](https://developers.giphy.com/docs/api#quick-start-guide).

After you have the API key in your hands, you can start writing some code to consume this API. However, sometimes you want to run some tests before you implement a lot of code. I know I do. The thing is, a few APIs will actually provide you with tools to fetch API data directly from the documentation or their dashboard.

In this particular case, GIPHY provides you with an [API Explorer](https://developers.giphy.com/explorer) that, after you create your app, allows you to start consuming the API without writing a line of code.

Some other APIs will provide you with explorers within the documentation itself, which is what [TheDogAPI](https://docs.thedogapi.com/api-reference/breeds/breeds-search) does on the bottom of each API reference page.

In any case, you can always use code to consume APIs, and that’s what you’ll do here. Grab the API key from the dashboard and, by replacing the value of the API_KEY variable below, you can start consuming the GIPHY API:


```python
import requests
from dotenv import dotenv_values
config = dotenv_values("giphy.env")

endpoint = "https://api.giphy.com/v1/gifs/trending"
params = {"api_key": config['API_KEY'], "limit": 3, "rating": "g"}
response = requests.get(endpoint, params=params).json()

for gif in response["data"]:
    title = gif["title"]
    trending_date = gif["trending_datetime"]
    url = gif["url"]
    print(f"{title} | {trending_date} | {url}")
```

At the top of the file, on lines 4 and 5, you define your API_KEY and the GIPHY API endpoint since they won’t change as often as the rest.

On line 7, making use of what you learned in the query parameters section, you define the params and add your own API key. You also include a couple of other filters: limit to get 3 results and rating to get only appropriate content.

Finally, after getting a response, you iterate through the results on line 9. For each GIF, you print its title, date, and URL on line 13.

Running this piece of code in the console would output a somewhat structured list of GIFs:

Now, let’s say you want to make a script that allows you to search for a specific word and fetch the first GIPHY match to that word. A different endpoint and slight variation of the code above can do that quite quickly:


```python
import requests
from dotenv import dotenv_values
config = dotenv_values("giphy.env")

endpoint = "https://api.giphy.com/v1/gifs/search"

search_term = "shrug"
params = {"api_key": config['API_KEY'], "limit": 1, "q": search_term, "rating": "g"}
response = requests.get(endpoint, params=params).json()

for gif in response["data"]:
    title = gif["title"]
    url = gif["url"]
    print(f"{title} | {url}")
```

There you have it! Now you can modify this script to your liking and generate GIFs on demand. Try fetching GIFs from your favorite show or movie, adding a shortcut to your terminal to get the most popular GIFs on demand, or integrating with another API from your favorite messaging system—WhatsApp, Slack, you name it. Then start sending GIFs to your friends and coworkers!

### Getting COVID-19 Confirmed Cases Per Country

Even though this may be something that you’re tired of hearing about by now, there’s a [free API](https://covid19api.com/) with up-to-date world COVID-19 data. This API doesn’t require authentication, so it’s pretty straightforward to get some data right away. The free version that you’ll use below has a rate limit and some restrictions on the data, but it’s more than enough for small use cases.

For this example, you’ll get the total number of confirmed cases up to the previous day. I randomly picked Germany again as the country, but you can pick any [country slug](https://api.covid19api.com/countries) you like:


```python
import requests
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
country = "germany"
endpoint = f"https://api.covid19api.com/country/{country}/status/confirmed"
params = {"from": str(yesterday), "to": str(today)}

response = requests.get(endpoint, params=params).json()
total_confirmed = 0
for day in response:
    cases = day.get("Cases", 0)
    total_confirmed += cases

print(f"Total Confirmed Covid-19 cases in {country}: {total_confirmed}")
```

    Total Confirmed Covid-19 cases in germany: 5923564


On lines 1 and 2, you import the necessary modules. In this case, you have to import the date and timedelta objects to be able to get today’s and yesterday’s dates.

On lines 6 to 8, you define the country slug you want to use, the endpoint, and the query parameters for the API request.

The response is a list of days, and for each day you have a Cases field that contains the total number of confirmed cases on that date. On line 11, you create a variable to keep the total number of confirmed cases, and then on line 14 you iterate through all the days and sum them up.

Printing the end result will show you the total number of confirmed cases in the selected country:

In this example, you’re looking at total number of confirmed cases for a whole country. However, you could also try looking at the [documentation](https://documenter.getpostman.com/view/10808728/SzS8rjbc) and fetching the data for your specific city instead. And why not make it a bit more thorough and get some other data, such as the number of recovered cases?

### Searching Google Books

If you have a passion for books, then you might want a quick way to search for a specific book. You might even want to connect it to your local library’s search to see if a given book is available using the book’s [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number).

For this example, you’ll use the [Google Books API](https://developers.google.com/books) and the [public volumes](https://developers.google.com/books/docs/v1/using#WorkingVolumes) endpoint to do simple searches of books.

Here’s a straightforward piece of code to look for the words moby dick in the whole catalog:


```python
import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"
query = "moby dick"

params = {"q": query, "maxResults": 3}
response = requests.get(endpoint, params=params).json()
for book in response["items"]:
    volume = book["volumeInfo"]
    title = volume["title"]
    published = volume["publishedDate"]
    description = volume["description"]
    print(f"{title} | ({published}) | {description[:30]}")
```

    Moby Dick | (2014-11-29) | Moby-Dick; or, The Whale is a 
    Moby Dick | (2016-06-17) | Moby Dick is a novel by Americ
    Why Read Moby-Dick? | (2013-09-24) | A “brilliant and provocative” 


This code example is pretty similar to the ones you’ve seen before. You start on lines 3 and 4 by defining important variables, such as the endpoint and, in this case, the query.

After making the API request, on line 8 you start iterating through the results. Then, on line 13, you print the most interesting information for each book that matches your initial query:

You can print the book variable inside the loop to see what other fields you have available. Here are a few that could be useful for further improving this code:

* industryIdentifiers
* averageRating and ratingsCount
* imageLinks

A fun challenge to do with this API is to use your [OAuth knowledge](https://developers.google.com/books/docs/v1/using#auth) and create your own bookshelf app that keeps records of all the books you read or want to read. You can even connect it to your favorite bookstore or library afterward to quickly find books from your wish list that are available near you. This is just one idea—I’m sure you can come up with more.

## Conclusion

There are a million other things you can learn about APIs: different headers, different content types, different authentication techniques, and so on. However, the concepts and techniques you learned in this tutorial will allow you to practice with any API of your liking and to use Python for any API consumption needs you may have.

In this tutorial, you learned:

* What an API is and what can you use it for
* What status codes, HTTP headers, and HTTP methods are
* How can you use Python to consume public data using APIs
* How to use authentication when consuming APIs with Python

Go ahead and try this new magic skill with some public APIs of your liking! You can also review the examples you saw in this tutorial by downloading the source code from the link below:

## Further Reading

The APIs used as examples in this tutorial are just a tiny fraction of the numerous public APIs available for free. Here’s a list of API collections that you can use to find your next favorite API:

* [GitHub Public APIs repository](https://github.com/public-apis/public-apis)
* [Public APIs](https://public-apis.io/)
* [Public API](https://public-apis.xyz/)
* [Any API](https://any-api.com/)

You can check these out and find an API that speaks to you and your hobbies and maybe inspires you to do a small project with it. If you come across a good public API that you think I or other people reading the tutorial should know about, then please leave a comment below!


```python

```

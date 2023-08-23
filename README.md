# Using and Testing Web Services - Tutorial


---

# **Introduction**
In the dynamic world of technology, web services act as bridges that effortlessly connect applications and devices. They dismantle barriers, enabling seamless data sharing across different platforms.

These services are fundamental for streamlined digital operations. By standardizing communication between applications, they enhance flexibility and scalability.

This tutorial serves as your comprehensive guide to effectively using and testing web services. You'll gain foundational knowledge and discover how to ensure their optimal performance. We'll delve into various types of web services, their integration into applications, and the essential aspect of testing for reliability.

By the end of this journey, you'll be equipped to navigate the intricacies of web services confidently, contributing to enhanced software experiences. Join us in this exploration of web services for a deeper understanding of their role in modern technology.

---

## Understanding Web Services

- What Are Web Services

Web services are a fundamental technology that facilitates seamless communication and data exchange between different software applications over the internet. They provide a standardized approach for diverse systems to interact, regardless of their underlying technologies.
Web services are protocols and standards that enable applications to communicate across different platforms, programming languages, and geographical locations. They ensure interoperability and seamless interaction between software systems.

- Types of Web Services: SOAP, REST, GraphQL
  - _SOAP (Simple Object Access Protocol):_ SOAP is a structured protocol for exchanging information using XML-based messaging. It's favored in enterprise-level applications for its reliability and security features.
  - _REST (Representational State Transfer):_ REST is an architectural style that uses standard HTTP methods (GET, POST, PUT, DELETE) to communicate with resources represented by URLs. It's known for its simplicity and scalability.
  - _GraphQL:_ GraphQL is a query language for APIs that allows clients to request specific data, reducing over-fetching or under-fetching of information.

- Why should we use Web Services in Applications?
  Web services offer several advantages in modern software development:
  - **Interoperability:** Different applications can communicate seamlessly, regardless of their technology stack.
  - **Modularity and Reusability:** Web services can be modularized and reused across multiple applications.
  - **Scalability:** Services can be scaled independently to handle varying levels of demand.
  - **Platform Independence:** Web services use standardized protocols, making them suitable for cross-platform development.
  - **Global Accessibility:** Web services can be accessed over the internet, enabling global connectivity.

---

**Understanding REST in Communication**

In the realm of modern digital connectivity, the Representational State Transfer (REST) architectural style stands as a guiding principle for designing networked applications. REST simplifies the interaction between software applications through a set of constraints, fostering a structured and efficient approach to communication. At its core, REST emphasizes the utilization of standard HTTP methods for resource manipulation, creating a consistent and intuitive framework for data exchange.

RESTful communication relies on a client-server model where clients, often web browsers or applications, initiate requests to servers. These requests carry specific HTTP methods that define the desired action, such as retrieving, creating, updating, or deleting resources. Servers, in response, provide well-structured data, often in formats like JSON or XML, ensuring seamless interpretation by the client.

**Decoding Interaction: HTTP Status Codes**

In this symbiotic communication between clients and servers, the language of HTTP status codes emerges as a critical tool for conveying the outcomes of each interaction. These three-digit numerical codes encapsulate the result of an HTTP request, serving as a common language for both clients and developers to understand the state of affairs. Let's delve into key categories and explore examples of HTTP status codes:

**1. Informational Responses (1xx):**
   - **100 Continue:** Acknowledgment of the initial request, indicating the server's readiness for further data transmission.

**2. Successful Responses (2xx):**
   - **200 OK:** Successful processing of the request, with the server delivering the desired data in the response body.
   - **201 Created:** The request leads to the establishment of a new resource on the server.
   - **204 No Content:** Although successful, no data needs to be included in the response body.

**3. Redirection Responses (3xx):**
   - **301 Moved Permanently:** The requested resource has undergone a permanent relocation to a new URL.
   - **302 Found (or 303 See Other):** Temporary redirection to a different URL for the requested resource.
   - **304 Not Modified:** The client's cached resource version remains valid, resulting in a response without re-transmission.

**4. Client Error Responses (4xx):**
   - **400 Bad Request:** The server struggles to comprehend the client's request due to errors or malformed syntax.
   - **401 Unauthorized:** Access requires valid authentication credentials.
   - **403 Forbidden:** Authenticated client lacks the necessary permissions to access the resource.
   - **404 Not Found:** The requested resource is absent on the server.
   - **405 Method Not Allowed:** The requested HTTP method is incompatible with the resource.

**5. Server Error Responses (5xx):**
   - **500 Internal Server Error:** Unforeseen server error disrupts the request fulfillment.
   - **501 Not Implemented:** The server lacks the functionality to fulfill the request.
   - **503 Service Unavailable:** Temporary server unavailability due to maintenance or overload.

![Http Status Error](https://static.semrush.com/blog/uploads/media/3a/79/3a7950050980a0e2de37bc1a632cc321/original.png)

---

In this tutorial, we will be using Postman because it is a powerful and widely used API testing tool that provides a user-friendly interface, allowing easy sending of HTTP requests and testing of APIs. 

Postman allows us to cover various aspects of the testing process:

1. **Request Generation:** Postman lets you create requests with different HTTP methods (GET, POST, PUT, DELETE, etc.), headers, query parameters, and request bodies. This flexibility is essential for testing various scenarios and endpoints of an API.

2. **Data-Driven Testing:** Postman allows you to parameterize your requests using variables, making it easy to test multiple scenarios by changing input values without rewriting requests.

3. **Response Inspection:** You can view API responses, including response codes, headers, and formatted response bodies. This helps in quickly identifying issues and verifying correctness.

4. **Authentication Testing:** Postman supports a wide range of authentication methods, including basic authentication, API keys, OAuth 2.0, and more. You can simulate different authentication scenarios during testing.

5. **Automation and Testing Suites:** Postman enables you to write tests using JavaScript, validating the responses automatically. This is crucial for regression testing and ensuring consistent behavior across API changes.

6. **Collection and Environment Management:** You can organize your requests into collections, helping you manage and group related requests. Environments allow you to manage different sets of variables for different testing environments.

7. **Integration and Collaboration:** Postman provides features for sharing collections and collaborating with team members, streamlining the testing process in a collaborative environment.

But, what is API testing meaning for?
**API testing** is the process of evaluating an Application Programming Interface (API) to ensure it functions correctly, integrates smoothly with other systems, handles errors, maintains data integrity, and performs well under different conditions. This type of testing confirms that APIs meet their design specifications and work reliably within software applications. It involves validating functionality, security, performance, and compatibility, ultimately contributing to the quality and dependability of the software systems that rely on these APIs. APIs are crucial components of modern software development, as they enable different software systems to communicate and interact. APIs are fundamental to modern software development, enabling developers to build complex applications by leveraging the capabilities of various components and services without having to build everything from scratch. They play a crucial role in promoting interoperability and innovation in the technology landscape.

In summary, API testing ensures the reliability, functionality, security, and performance of APIs, contributing to the overall quality and stability of software systems that rely on them.

---
## **Making Your First HTTP Request**

In this tutorial we will use a simple open-source API to demonstrate the CRUD operations. CRUD stands for Create, Read, Update and Delete. 
- Create : (Post) Used to create a new resource, but can also modify the underlying state of a system.
- Read : (Get) Used to retrieve a representation of the resource.
- Update : (Put/Patch) Update an existing resource.
- Deleted : (Delete) Delete a resource.

## Prerequisites 
* **Installing a Web Browser:** In order to correctly test APIs, download a Web Browser such as Google Chrome
* **Installing and Configuring Postman:** Here's what you need to do for installing the API testing platform Postman:

  1. **Download and Install:** Go to the [Postman download page](https://www.postman.com/downloads/) and choose the version suitable for your operating system. Install it by following the on-screen instructions.

  2. **Sign Up/Login:** Once installed, open Postman. You can sign up for a free account or log in if you already have one. This allows you to sync your work across devices. Postman simplifies API testing by providing a user-friendly interface and a range of features that help you understand and interact with APIs effectively.

---

We can start with our tutorial by creating a Collection and some variables where we can save the more usefull requests and information.
Creating a collection in Postman is a fundamental step in organizing and managing your API requests. A collection is a container that holds a group of requests, allowing you to efficiently organize, execute, and maintain your API tests. Here's how to create a collection in Postman:

1. **Collections Tab:** In the left sidebar, click on the `Collections` tab. This is where you'll manage your collections.

2. **Create New Collection:** At the top of the `Collections` tab, you'll see a `New` button. Click on it to create a new collection.

3. **Name and Description:** A window will pop up prompting you to enter a name and an optional description for your collection. Provide a meaningful name that reflects the purpose of the collection.

4. **Add Requests to the Collection:** Once your collection is created, you can start adding requests to it. To do this, you can:

   - Create new requests directly within the collection.
   - Import requests from other sources like URLs or cURL commands.
   - Duplicate existing requests and modify them as needed.

   To add a request:
   
   - Click on the collection you created.
   - Click the `Add a request` button within the collection.
   - Give the request a name and specify the HTTP method, URL, headers, parameters, and body as required.

5. **Save and Use:** Make sure to save your collection and your requests. You can now use this collection to execute requests, organize your API testing workflow, and collaborate with others.

To create and use a variable, instead, do the following:

1. Click on the environment quick look icon located in the workbench.
2. Next to `Globals`, click on the `Edit` button (or `Add` if no variables are added yet).
3. Create a variable named `token` and type the value of the obtained token.
4. Click the `Save` icon, then close the environment tab.

In the URL field, you can use variables by using this syntax: {{name_variable}}. For example, if we save the base URL `https://simple-books-api.glitch.me` into the variable `baseUrl`, we can use it in the next requests like this: {{baseUrl}}/endpoint.

---

Many APIs require a subscription fee, making it crucial to obtain a personal key or token to access them. Usually, this key is added as a query parameter when interacting with the server.

To utilize these APIs, an access token is necessary. An access token is a string that holds vital credentials and permissions, enabling access to specific resources. The process of obtaining an access token involves user authentication. This authentication is carried out using a POST request, which typically includes login details like username and email in the request body. Through this process, an access token is acquired, enabling subsequent requests for specific resources. Here's how you can retrieve it:

1. **Create a New POST Request:**
   - In the request tab, you can provide a suitable name for your request, such as "API Client Registration."
   - Select the HTTP method as "POST". We will see the POST method in more detail later on.
3. **Set the Request URL:**
   - Enter the URL for the API endpoint: `{{baseUrl}}/api-clients/`.
4. **Add Request Body:**
   - In the request tab, select the "Body" tab below the URL field.
   - Choose the "raw" option and select "JSON" from the dropdown.
   - Copy and paste the example JSON body you provided earlier into the text area:
```
{
  "clientName": "your-clientName",
  "clientEmail": "your-email@example.com"
}
```
Upon successful registration, the response will provide an access token. This token remains valid for a period of 7 days.

With the acquired tokend, we're ready to delve into our tutorial. To initiate, let's execute a GET request to the `/status` endpoint.This will help us learn how to perform GET requests and check the current status of the API. 

1. **Create a New Request:**
   - Select the HTTP method as "GET."

2. **Set the Request URL:**
   - Enter the URL for the API endpoint you want to query. In this case, it's `{{baseUrl}}/status`.
  
If the request succeded, we get the status of the API. At this point, it is important to understand the response from the server.

WIn Postman, when you send requests to APIs, you might encounter different types of responses, including success responses and error responses. These responses are accompanied by status codes, which are standardized numerical codes that provide information about the outcome of the request. Status codes help you understand whether your request was successful or encountered an issue. Here's a brief overview of status codes in Postman:

1. **Success Response (2xx):** Receiving a `2xx` code (e.g., `200 OK`) denotes a successful request. You'll often find your anticipated data in the response body.

2. **Client Error (4xx):** A `4xx` code (e.g., `404 Not Found`) signifies a client-side glitch. It might mean the sought-after resource is absent (`404`), or authentication is lacking (`401 Unauthorized`).

3. **Server Error (5xx):** A `5xx` code (e.g., `500 Internal Server Error`) signals server-side issues. These could stem from misconfigured settings or backend snags.

4. **Other Codes (1xx, 3xx):** Less frequent, these codes in the `1xx` and `3xx` range have distinct roles in communication and redirection scenarios.

---
Try it yourself.

### EXERCISE 1: **List Books:**
Looking at [Book APIs documentation](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md), try to retrieve the list of available books.

---

**Understanding and Utilizing Path Parameters in URLs**

Path parameters are a powerful tool for creating dynamic and precise URLs that help you access specific resources. They are variable segments within the path of a URL that enable you to pass dynamic values that act as identifiers for specific resources. 

To set up a path parameter, you use key-value pairs directly within the URL path. Suppose you are working with an API that provides information about books, and you want to retrieve details about a specific book using its unique ID. Here's how you would structure the URL with a path parameter:
```
https://example-book-api.com/books/:bookID
```

In practical terms, this means replacing `:bookID` with the actual ID value when crafting your request.

Working with path parameters becomes remarkably seamless when using tools such as Postman. The process involves effortlessly integrating the parameters into your request URL and replacing them with the appropriate corresponding values.

It's crucial to use the correct path parameter values. If you use the wrong value or format, the server will respond with a "404: Not Found" error. This is because the server cannot locate the resource you're trying to access.

Now, let's put this knowledge into action with an exercise.

### **Exercise 2: Exploring Book Information**

Refer to the [Book APIs documentation](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md) try to retrieve detailed information about the book with the ID of 2.

--

**Query Parameters:**

Query parameters are additional details you can attach to a URL in Postman. They're key-value pairs that come after a question mark (`?`) in the URL. These parameters customize your API requests by providing extra information to the server.

**How to Use Them in Postman:**
Assuming you're working with the Book API and you want to retrieve a list of books based on different filters.

1. **Open Postman:**
   Launch Postman and either create a new request or open an existing one.

2. **Select the "Params" Tab:**
   In the request window, click on the "Params" tab located below the URL field.

3. **Add Query Parameters:**
   In the "Params" tab, you'll see two columns: "Key" and "Value". Here's how you might add query parameters for filtering books:
   - **Key:** genre
     **Value:** thriller
   - **Key:** author
     **Value:** Stephen King

   You can continue adding more parameters as needed.

4. **Review URL:**
   As you add the query parameters, observe that the URL in the main URL field automatically updates to include the parameters. It should look something like:
   ```
   https://example-book-api.com/books?genre=thriller&author=Stephen%20King
   ```
Note that spaces are automatically encoded as `%20` to ensure proper formatting.

---
Try it yourself.

### EXERCISE 3: **List Books:**
Looking at [Book APIs documentation](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md), try to retrieve the list of available books of non-fiction genre.

---

To conclude, we can send data, such as JSON or form data, to the server by adding a request body to the request. This is often used in HTTP methods like POST, PUT, and PATCH to update or create resources. It can be dane by clicking on the "Body" tab and choosing the format of the data you're sending in the request body. Common formats include JSON, form-data, x-www-form-urlencoded, and raw text.

---
Try it yourself.

### EXERCISE 4: **Order a book:**
Looking at [Book APIs documentation](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md), try to create a new order. Remember that this process involves authenticating with an access token and providing necessary order details in JSON format.

### EXERCISE 5: **Order changes:**
Looking at [Book APIs documentation](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md), try to change the customer's name of the first order in "Mario".

### EXERCISE 6: **Delete order:**
Looking at [Book APIs documentation](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md), try to delete the last order submitted.

---



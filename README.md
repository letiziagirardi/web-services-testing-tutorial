# Using and Testing Web Services - Tutorial


---

# **Web services**
Web services are a fundamental component of modern software architecture that enable different applications or systems to communicate and share data over the internet. They serve as a bridge between various platforms, allowing them to interact with each other regardless of the technologies they are built upon. Web services play a crucial role in enabling interoperability and data exchange in distributed computing environments.

## **Here are some key characteristics for understanding web services:**
 
* **Interoperability:** Web services are designed to work across different programming languages, operating systems, and platforms. This means that applications written in different technologies can communicate seamlessly through web services.

* **Communication Protocol:** Web services use standardized communication protocols, most commonly HTTP or HTTPS, to exchange data. This makes it easy to transmit data over the internet.

* **Data Format:** Web services use standard data formats for data exchange, such as XML (eXtensible Markup Language) or JSON (JavaScript Object Notation). These formats ensure that data is structured and can be understood by both the sender and receiver.

* **API (Application Programming Interface):** Web services are often accessed using APIs, which define how different software components should interact with each other. APIs provide a set of functions and protocols for building and integrating software.

* **Types of Web Services:** There are different types of web services based on their functionality. These include:
  * _SOAP (Simple Object Access Protocol):_ SOAP is a structured protocol for exchanging information using XML-based messaging. 
  * _REST (Representational State Transfer):_ REST is an architectural style that uses standard HTTP methods (GET, POST, PUT, DELETE) to communicate with resources represented by URLs. It's known for its simplicity and scalability.
  * _GraphQL:_ GraphQL is a query language for APIs that allows clients to request specific data, reducing over-fetching or under-fetching of information.

 
## **Why should we use Web Services in Applications?**
  Web services offer several advantages in modern software development:
  * **Interoperability:** Different applications can communicate seamlessly, regardless of their technology stack.
  * **Modularity and Reusability:** Web services can be modularized and reused across multiple applications.
  * **Scalability:** Services can be scaled independently to handle varying levels of demand.
  * **Platform Independence:** Web services use standardized protocols, making them suitable for cross-platform development.
  * **Global Accessibility:** Web services can be accessed over the internet, enabling global connectivity.

---

## **Understanding REST in Communication**
In our tutorial, we will focus on REST architecture because it simplifies the interaction between software applications through a set of constraints, fostering a structured and efficient approach to communication. At its core, REST emphasizes the utilization of standard HTTP methods for resource manipulation, creating a consistent and intuitive framework for data exchange.

RESTful communication relies on a client-server model where clients, often web browsers or applications, initiate requests to servers. These requests carry specific HTTP methods that define the desired action. Servers, in response, provide well-structured data, often in formats like JSON or XML, ensuring seamless interpretation by the client.

**Decoding Interaction: HTTP Status Codes**

In this symbiotic communication between clients and servers, the language of HTTP status codes allows to convey the outcomes of each interaction.
The main examples of HTTP status codes are:

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
This tutorial is designed to provide you with the knowledge and skills necessary to effectively interact with APIs. Throughout this tutorial, you'll gain a solid understanding of the concepts that underpin APIs and learn practical techniques for interacting with them. We'll cover various aspects, from making simple API requests to handling more complex scenarios like authentication, error handling, and data manipulation.

By the end of this journey, you'll be equipped with the tools to confidently communicate with APIs, retrieve and exchange data, and integrate external functionalities into your own projects. 
---

Before delving into the technical details, let's try to understand two fundamental concepts: what an API is and the significance of API testing.

**What is an API?**

An API, or Application Programming Interface, is a bridge that enables different software systems to communicate and interact with each other. Think of it as a language that allows various applications to share data and functionalities seamlessly. Just as a waiter acts as an intermediary between you and the kitchen in a restaurant, an API facilitates communication between different software components, even if they're developed using different technologies.

**What is API Testing?**

API testing is the process of rigorously assessing the reliability, functionality, and performance of APIs. Much like quality control for products, API testing ensures that APIs operate as expected. It involves sending specific requests to an API and analyzing the responses it generates. By doing so, we verify that APIs deliver accurate and consistent results while adhering to predefined standards.

With these foundational concepts in mind, we're ready to explore the technical aspects of diverse open-source APIs, all orchestrated through the versatile platform of Postman.

## **Postman**
**What is Postman?**
Postman is a versatile and widely-used software tool designed to simplify the process of developing, testing, and documenting APIs (Application Programming Interfaces). It provides developers, testers, and API consumers with a user-friendly interface for interacting with APIs, making the testing and integration of APIs more efficient and effective.

At its core, Postman offers the following key functionalities:

1. **API Requests:** Postman allows users to send various types of API requests, including GET, POST, PUT, and DELETE requests. These requests can be tailored to specific API endpoints, enabling users to interact with APIs and retrieve or manipulate data.

2. **Request Customization:** Users can customize API requests by adding headers, parameters, request bodies, authentication details, and more. This flexibility ensures that requests can be accurately configured to match API requirements.

3. **Response Inspection:** Postman provides a visual representation of API responses, making it easy to analyze and verify data returned by the API. Responses are often displayed in formats like JSON or XML for easy interpretation.

4. **Collection Organization:** Postman allows users to organize related requests into collections, making it convenient to manage and execute multiple requests as part of a workflow or test suite.

5. **Environment Variables:** Users can set up environment variables to store and reuse values across requests. This is particularly useful for scenarios where data from one request needs to be used in subsequent requests.

6. **Automation:** Postman supports test scripting using JavaScript, enabling users to create automated test suites to validate API responses. This is essential for ensuring the correctness and reliability of APIs.

7. **API Documentation:** Postman can automatically generate API documentation based on the requests and descriptions provided by users. This documentation is helpful for sharing API information with other developers.

We are going to present each key functionality of Postman throughout the tutorial in order to guide the audience through a comprehensive understanding of Postman's functionalities. 
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

## **Automating Tests in Postman**
In Postman it is possible to perform tests on software applications, systems, or components by using automated tools and scripts. Test automation is commonly used in software development to ensure the quality, reliability, and efficiency of software products.

**1. Creating Test Scripts:**

Postman allows you to create test scripts for each API request using JavaScript. These scripts are executed after sending a request and can be used to verify the response's correctness, status, and other attributes. Here's how you can create a test script within Postman:

1. **Navigate to "Tests" Tab:** In the request editor, switch to the "Tests" tab. This is where you'll write your test scripts.

2. **Write Your Test Script:** Use JavaScript to write your test script. For example, to check the response status code and verify the presence of certain data in the response, you can write:

```
// Check response status code
pm.test("Status code is 200 OK", function () {
    pm.response.to.have.status(200);
});

// Verify presence of specific data in response JSON
pm.test("Response body contains expected data", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.key).to.eql("expectedValue");
});
```

3. **Execute the Request:** After writing the test script, you can click the "Send" button to execute the request. Postman will send the request to the API and then run your test scripts to validate the response.

**2. Chaining Requests:**

Chaining requests in Postman involves using the response from one request as input for subsequent requests. This is useful for scenarios where you need to perform a sequence of API calls. Here's how you can chain requests and automate scenarios:

1. **Create Multiple Requests:** Create the API requests you want to chain. Let's say you have two requests: "Request A" and "Request B".

2. **Reference Response Data:** In "Request A", you can save data from the response using Postman variables. For example, if the response contains an "id" that you want to use in "Request B", you can save it like this in the "Tests" tab of "Request A":

```
var responseJson = pm.response.json();
pm.environment.set("savedId", responseJson.id);
```

3. **Chaining Requests:** In "Request B", you can reference the saved data in "Request A" using the Postman variable. You might include this variable in the URL or headers, depending on your use case:

```
// Use the saved ID from Request A
var savedId = pm.environment.get("savedId");

// Now use this ID in your request URL or headers
pm.sendRequest({
    url: "https://api.example.com/resource/" + savedId,
    method: "GET"
});
```

4. **Execute Chained Requests:** When you execute "Request A", the response data is saved to the environment variable. Then, when you execute "Request B", it uses the saved data from the environment variable to build the URL or headers.

This way, you can automate scenarios where data from one request is needed in subsequent requests, creating a chain of automated API calls.

---

### EXERCISE 6: **Delete order:**
Looking at [Book APIs documentation](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md), get the book information as follow:
- Retrieve the id of the book "Just as I Am"
- Order the book based on the saved variable id

---

## **API Documentation**

Imagine embarking on a journey without a map or clear directions. Similarly, navigating the realm of software development without proper API documentation can leave developers feeling disoriented and frustrated.

API documentation acts as a guiding light, illuminating the path for developers seeking to interact with an API. It's more than just instructions; it's a comprehensive handbook that unveils the API's endpoints, data structures, authentication methods, and more. Its significance is profound for several reasons.

Primarily, well-documented APIs drastically reduce the learning curve. Developers can swiftly grasp how to make requests, avoiding the frustrating trial-and-error process. This efficiency enables quicker integration and empowers developers to channel their creativity.

Additionally, accurate documentation serves as a shield against errors. Developers can confidently implement API calls, knowing they've interpreted instructions correctly. This clarity enhances the overall reliability of applications.

Moreover, comprehensive API documentation fosters community and collaboration. Developers share insights and best practices, nurturing a culture of mutual learning.

The more popular API documentation tools are Postman API, Swagger, and Stoplight. Let's dive deeper into them.

### **Postman API Documentation:**
Postman offers features for easy creating, publishing and sharing comprehensive API documentation.

**Key Features:**
- **Auto-generate Documentation:** Postman can generate API documentation directly from the requests and responses you create during testing.
- **Customizable:** You can edit and enhance the generated documentation with additional information, examples, and explanations.
- **Interactive Examples:** Documentation includes interactive examples that allow users to make API requests within the documentation itself.
- **Sharing:** Documentation can be easily shared with team members, stakeholders, and external developers.
- **Hosted Docs:** Postman provides an option to host API documentation on their servers, ensuring accessibility.

**Advantages:**
- Seamlessly combines API testing and documentation in one tool.
- Allows real-time testing within the documentation itself.
- User-friendly interface for creating and managing documentation.

### **Swagger (OpenAPI):**
Swagger, now known as OpenAPI, is an open-source specification for designing, documenting, and testing APIs. It provides a standardized way to describe APIs that developers can use to create interactive documentation and generate client SDKs.

**Key Features:**
- **Standardized Specification:** OpenAPI provides a standardized format for describing API endpoints, parameters, request and response formats, authentication, and more.
- **Interactive Documentation:** Swagger UI, a tool built on top of OpenAPI, creates interactive and user-friendly API documentation.
- **Code Generation:** Swagger Codegen can generate client libraries, server stubs, and API documentation from the OpenAPI specification.
- **API Testing:** Some tools integrate API testing features, allowing you to validate your API against its specification.

**Advantages:**
- Widely adopted in the industry as a de facto standard for API documentation.
- Supports a wide range of programming languages and frameworks.
- Promotes consistency and reduces ambiguity in API communication.

### **Stoplight:**
Stoplight is a platform designed to help organizations create, manage, and publish API documentation. It aims to streamline the entire API lifecycle, from design to testing to documentation.

**Key Features:**
- **Visual Design:** Stoplight offers a visual designer for API specifications, making it easier to define endpoints and data models.
- **Collaboration:** Teams can collaborate on API design, documentation, and testing in real-time.
- **Mock Servers:** Stoplight can generate mock servers based on your API specification for testing and development.
- **API Governance:** Provides tools to ensure API design consistency and adherence to company standards.

**Advantages:**
- Offers an end-to-end solution for the API development process.
- Encourages collaboration between development, testing, and documentation teams.
- Provides mock server capabilities for early-stage testing.











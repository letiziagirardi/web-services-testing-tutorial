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

In this tutorial we will use Spotify's open-source API to demonstrate the CRUD operations. CRUD stands for Create, Read, Update and Delete. 
- Create : (Post) Used to create a new resource, but can also modify the underlying state of a system.
- Read : (Get) Used to retrieve a representation of the resource.
- Update : (Put/Patch) Update an existing resource.
- Deleted : (Delete) Delete a resource.

## Prerequisites 
* **Installing a Web Browser:** In order to correctly test APIs, download a Web Browser such as Google Chrome
* **Creating a Spotify account:** This tutorial assumes you have a Spotify account (free or premium).
* **Installing and Configuring Postman:** Here's what you need to do for installing the API testing platform Postman:

  1. **Download and Install:** Go to the [Postman download page](https://www.postman.com/downloads/) and choose the version suitable for your operating system. Install it by following the on-screen instructions.

  2. **Sign Up/Login:** Once installed, open Postman. You can sign up for a free account or log in if you already have one. This allows you to sync your work across devices. Postman simplifies API testing by providing a user-friendly interface and a range of features that help you understand and interact with APIs effectively.

---

To use these APIs we need to get a user ID and OAuth token. 
The steps to do for using them are the following:
- Create an app, if you haven't done so.
- Request an access token.
- Use the access token to request the artist data.
  
### **Create an app**

To obtain an access token via the implemented authorization flows, you'll need to create an app. Here's how:
* Access your Dashboard and click "Create an app."
* Fill in the details:
   - App Name: My App
   - App Description: This is my first Spotify app
   - Redirect URI: Use http://localhost:3000 for now (not required in this example).
* Make sure to agree to the Developer Terms of Service.
* Click "Create."

### **Request an access token**
An access token functions as a string containing essential credentials and permissions, providing the means to access specific resources (such as artists, albums, or tracks) or a user's data (like profiles or playlists).

To initiate the access token request, you'll require your Client ID and Client Secret. Here's how you can retrieve them:

* Head over to the Dashboard.
* Click on the name of your freshly created app (My App).
* Opt for the Settings button.
* Your Client ID is displayed here, while your Client Secret is accessible via the "View client secret" link.

With our credentials in hand, we are ready to request an access token. This tutorial uses the Client Credentials, so we must:
* Send a POST request to the token endpoint URI.
* Add the Content-Type header set to the application/x-www-form-urlencoded value.
* Add a HTTP body containing the Client ID and Client Secret, along with the grant_type parameter set to client_credentials.

### Obtain an Access Token
With our credentials in hand, we are ready to request an access token. This tutorial uses the Client Credentials, so we must:
- Send a POST request to the token endpoint URI.
   - Choose "POST" from the dropdown menu next to the URL bar.
   - Enter the URL: `https://accounts.spotify.com/api/token`.
- Add the Content-Type header set to the application/x-www-form-urlencoded value.
   - In the Params section, click on the "Key" column and enter `Content-Type`.
   - In the "Value" column, enter `application/x-www-form-urlencoded`.
    ![Parameters](https://github.com/letiziagirardi/web-services-testing-tutorial/assets/71395970/cfd53896-739e-4e6c-953b-b17867c7ab39)

- Add a HTTP body containing the Client ID and Client Secret, along with the grant_type parameter set to client_credentials.
   - Select "x-www-form-urlencoded" as the body type.
   - Add the following parameters:
     - Key: `grant_type`, Value: `client_credentials`
     - Key: `client_id`, Value: `your-client-id`
     - Key: `client_secret`, Value: `your-client-secret`

   Replace `your-client-id` and `your-client-secret` with your actual Spotify app's Client ID and Client Secret.
  ![Body](https://github.com/letiziagirardi/web-services-testing-tutorial/assets/71395970/543dcee0-5ca7-4227-a86a-01f22b8f6f30)

When you successfully request an access token using the Client Credentials flow, the response will look like this:

```json
{
    "access_token": "BQDkQvl8qHTViptgh1xpCT0bn0ASbUk4l4kwwVKy-FInkwZm6y06CK9e6tyjPLi1-MC5QraAfViX4d_CLujlSap99Q8Xv1OT1S_qKGiEDvYXC9anEKw",
    "token_type": "Bearer",
    "expires_in": 3600
}
```
The response will return an access token valid for 1 hour.








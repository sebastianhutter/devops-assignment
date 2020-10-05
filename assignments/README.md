# Assignments

We prepared a few assignments for you. Feel free to document your progress in any shape or form. We will be reviewing the assignments together.

## 1 - Build the application

Your first task is to build the demo application and push the resulting docker image to your docker registry.

## 2 - Deploy the application

Deploy the application to the kubernetes cluster and access it with a port-forward.

## 3 -  Expose the application to the internet

Expose the deployed application to the internet.

`Tip`: We are using a digitalocean kubernetes cluster - have a look at their docs.

## 4 - Configure the application

The application shows a violet banner with the text `LOCAL`. Change the color of the banner to `blue` and the text to `DIGITALOCEAN`.

## 5 - Add liveness and readiness probes

Add a liveness and readiness probe to the kubernetes pod.

`Tip`: We are working with a spring boot application. Have a look at the spring boot actuator!

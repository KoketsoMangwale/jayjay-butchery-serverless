
# 🥩 Jay Jay Factory Butchery - Serverless eCommerce Backend

This repository contains a **serverless eCommerce backend** for  
**Jay Jay Factory Butchery**, a local butchery expanding its services online.  

The backend is built using **AWS SAM** with **Python**, **DynamoDB**, **API Gateway**, **Lambda**, and **SNS**.

---

## 🚀 Features
- 📦 Manage product catalog in DynamoDB
- 🛒 Customers can place orders via API
- 📧 Order notifications via Amazon SNS
- 🌍 REST API powered by API Gateway + Lambda (Python)
- 🔒 CORS enabled for frontend integration (S3/CloudFront)

---

## 🏗️ Architecture
- **Amazon API Gateway** – REST API endpoints  
- **AWS Lambda (Python 3.12)** – business logic  
- **Amazon DynamoDB** – products & orders database  
- **Amazon SNS** – order notifications (email/SMS)  
- **Amazon S3/CloudFront** (frontend to be added separately)

---

## 📂 Project Structure
```

jayjay-butchery-serverless/
├── src/
│   ├── list_products/    # Lambda for GET /products
│   ├── place_order/      # Lambda for POST /order
│   └── get_orders/       # Lambda for GET /orders
├── events/
│   └── place-order.json  # Sample test event
├── template.yaml         # SAM template
└── README.md             # Documentation

````

---

## ⚙️ Prerequisites
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) configured  
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed  
- Python 3.12  

---

## 🚀 Deployment

```bash
# Build the project
sam build

# Deploy with guided parameters
sam deploy --guided
````

Recommended parameters:

* **Stack Name:** `jayjay-butchery-backend`
* **Region:** `af-south-1` (Cape Town)
* **StageName:** `prod`
* **ProductsTableName:** `ButcheryProducts`
* **OrdersTableName:** `Orders`
* **CorsAllowOrigin:** `*` (or restrict to your CloudFront domain)
* **SnsTopicName:** `JayJayOrdersTopic`

---

## 🧪 Testing

### List products

```bash
curl "$API_BASE_URL/products"
```

### Create order

```bash
curl -X POST "$API_BASE_URL/order" \
  -H "Content-Type: application/json" \
  -d '{
    "customerName":"Koketso",
    "customerPhone":"+27-82-000-0000",
    "items":[
      {"productId":"steak-001","name":"Rump Steak","quantity":2,"price":129.99}
    ],
    "notes":"Please vacuum seal."
  }'
```

### Get orders

```bash
curl "$API_BASE_URL/orders"
```

---

## 🥩 Seeding Products

Add sample product into DynamoDB:

```bash
aws dynamodb put-item --table-name ButcheryProducts --item '{
  "productId": {"S":"steak-001"},
  "name": {"S":"Rump Steak"},
  "price": {"N":"129.99"},
  "unit": {"S":"per kg"},
  "category": {"S":"beef"},
  "active": {"BOOL": true}
}'
```

---

## 📧 Notifications

* An **SNS Topic** is created (`JayJayOrdersTopic`).
* Subscribe your email or SMS to receive order notifications.

---

## 🔮 Next Steps

* [ ] Add static frontend (S3 + CloudFront)
* [ ] Secure admin routes with Cognito authorizer
* [ ] Integrate payment gateway (PayFast/Stripe)
* [ ] Add product images (S3 bucket)

---

## 📜 License

MIT License – free to use and adapt.

```

---

Do you also want me to add a **frontend starter repo** suggestion (like `jayjay-butchery-frontend`) with an S3-ready template wired to this API?
```

<!-- Improved compatibility of back to top link -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ThomasGates3/SpeakEasy-TTS">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">SpeakEasy - AWS Text-to-Speech Converter</h3>

  <p align="center">
    A serverless text-to-speech converter built with AWS services for optimal cost and performance.
    <br />
    <a href="https://github.com/ThomasGates3/SpeakEasy-TTS"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ThomasGates3/SpeakEasy-TTS">View Demo</a>
    ·
    <a href="https://github.com/ThomasGates3/SpeakEasy-TTS/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/ThomasGates3/SpeakEasy-TTS/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#architecture-overview">Architecture Overview</a></li>
    <li><a href="#why-serverless">Why Serverless?</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#challenges-and-solutions">Challenges and Solutions</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

---

## About The Project

[![SpeakEasy Screenshot][product-screenshot]](images/speakeasy-screenshot.png)

This project demonstrates a **modern serverless text-to-speech converter** that transforms written text into natural-sounding audio using Amazon Polly. The application features a clean, dark-themed interface and leverages AWS's powerful cloud services for optimal performance and cost efficiency.

**Key Features:**
- High-quality text-to-speech conversion using Amazon Polly
- Serverless architecture for scalability and cost optimization  
- Modern, responsive dark theme interface
- Fast audio generation and playback
- Pay-per-use pricing model
- Secure AWS-managed infrastructure

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

### Built With

* [![HTML5][HTML5]][HTML5-url]
* [![CSS3][CSS3]][CSS3-url]
* [![JavaScript][JavaScript]][JavaScript-url]
* [![AWS Lambda][Lambda]][Lambda-url]
* [![Amazon API Gateway][APIGateway]][APIGateway-url]
* [![Amazon Polly][Polly]][Polly-url]
* [![Amazon S3][S3]][S3-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

### Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │───▶│   API Gateway    │───▶│   AWS Lambda    │
│   (HTML/CSS/JS) │    │                  │    │   (Python)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                                                         ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   End User      │◀───│   Amazon S3      │◀───│   Amazon Polly  │
│   (Audio)       │    │   (Audio Files)  │    │   (TTS Service) │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

### Why Serverless?

**Cost Optimization**
- **Pay-per-use model**: Only pay when the service is actually used
- **No idle costs**: Traditional servers charge 24/7, even with zero traffic
- **Automatic scaling**: Resources scale to zero when not needed
- **Cost comparison**: A traditional EC2 instance costs ~$8.76/month minimum, while serverless can cost pennies for low-traffic applications

**Performance & Speed**
- **Global edge locations**: API Gateway provides low-latency access worldwide
- **Auto-scaling**: Handles traffic spikes without manual intervention
- **Cold start optimization**: Modern Lambda cold starts are typically <1 second
- **Managed services**: No time spent on server maintenance or updates

**Operational Simplicity**
- **Zero server management**: AWS handles all infrastructure concerns
- **Built-in monitoring**: CloudWatch provides comprehensive logging and metrics
- **Automatic backups**: S3 and Lambda configurations are automatically backed up
- **High availability**: Built-in redundancy across multiple availability zones

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Prerequisites
- AWS account with appropriate permissions
- Basic understanding of AWS services (Lambda, API Gateway, S3, IAM)
- Text editor for code modifications
- AWS CLI installed (optional but recommended)

### Installation

**Step 1: Clone the repository**
```sh
git clone https://github.com/ThomasGates3/SpeakEasy-TTS.git
cd SpeakEasy-TTS
```

**Step 2: Create S3 Bucket**
```sh
aws s3 mb s3://speakeasy-audio-files-yourname --region us-east-1
```

**Step 3: Configure S3 Bucket Policy**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
        }
    ]
}
```

**Step 4: Create Lambda Function with proper IAM role**
- Navigate to Lambda Console
- Create function with Python 3.9+ runtime
- Add environment variable: `S3_BUCKET_NAME`
- Set timeout to 30 seconds

**Step 5: Configure API Gateway**
- Create REST API
- Enable CORS with proper headers
- Deploy API to get invoke URL

**Step 6: Update frontend configuration**
```javascript
const apiGatewayEndpoint = "YOUR-API-GATEWAY-INVOKE-URL";
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Usage

Submit text for speech conversion:

```bash
# Open the web application
# Enter text in the textarea
# Click "Convert to Speech"
# Audio player will appear with generated speech
```

Application workflow:
1. Enter text to convert to speech
2. Click "Convert to Speech" button
3. Wait for conversion (usually 2-5 seconds)
4. Audio player appears with generated speech
5. Click play to listen to the result

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Challenges and Solutions

### The CORS Nightmare

**Problems Encountered:**
- Initial CORS Error: `Access to fetch blocked by CORS policy`
- 502 Bad Gateway even after enabling CORS in API Gateway
- OPTIONS preflight issues not being handled
- Inconsistent behavior between Postman and browser

**Solution Journey:**
1. **API Gateway CORS Settings** - Still failed because I forgot to deploy the API
2. **Lambda Function Headers** - Still failing because OPTIONS requests weren't handled
3. **Handle OPTIONS Method** - Finally working after proper implementation

**Final Working Solution:**
```python
if event.get('httpMethod') == 'OPTIONS':
    return {
        'statusCode': 200,
        'headers': cors_headers,
        'body': ''
    }
```

**Key Learnings:**
- Always deploy API Gateway changes
- Handle OPTIONS requests in Lambda
- Include CORS headers in ALL response paths
- Use browser dev tools Network tab for debugging

### Lambda Function Debugging

**Challenge**: Getting 502 errors with unclear error messages

**Solution**: Added comprehensive logging and error handling
```python
try:
    print(f"Debug info: {some_variable}")
except Exception as e:
    print(f"Error occurred: {str(e)}")
    import traceback
    print(f"Traceback: {traceback.format_exc()}")
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Roadmap

- [x] Basic text-to-speech functionality
- [x] CORS support for web browsers  
- [x] Error handling and logging
- [ ] Multiple voice selection
- [ ] SSML support for advanced speech control
- [ ] Audio format options (MP3, OGG, PCM)
- [ ] Rate limiting and usage analytics
- [ ] User authentication and personalized settings

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contact

Thomas Gates III - [thomas-gates-iii](https://linkedin.com/in/thomas-gates-iii) - thomasthethird3@gmail.com

Project Link: [https://github.com/ThomasGates3/SpeakEasy-TTS](https://github.com/ThomasGates3/SpeakEasy-TTS)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Acknowledgments

* Amazon Web Services for providing robust cloud infrastructure
* Amazon Polly for amazing text-to-speech capabilities  
* Best README Template for excellent structure
* AWS community for tutorials and troubleshooting guides
* Stack Overflow for helping solve CORS issues

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- MARKDOWN LINKS -->
[contributors-shield]: https://img.shields.io/github/contributors/ThomasGates3/SpeakEasy-TTS.svg?style=for-the-badge
[contributors-url]: https://github.com/ThomasGates3/SpeakEasy-TTS/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ThomasGates3/SpeakEasy-TTS.svg?style=for-the-badge
[forks-url]: https://github.com/ThomasGates3/SpeakEasy-TTS/network/members
[stars-shield]: https://img.shields.io/github/stars/ThomasGates3/SpeakEasy-TTS.svg?style=for-the-badge
[stars-url]: https://github.com/ThomasGates3/SpeakEasy-TTS/stargazers
[issues-shield]: https://img.shields.io/github/issues/ThomasGates3/SpeakEasy-TTS.svg?style=for-the-badge
[issues-url]: https://github.com/ThomasGates3/SpeakEasy-TTS/issues
[license-shield]: https://img.shields.io/github/license/ThomasGates3/SpeakEasy-TTS.svg?style=for-the-badge
[license-url]: https://github.com/ThomasGates3/SpeakEasy-TTS/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/thomas-gates-iii

[product-screenshot]: images/speakeasy-screenshot.png
[HTML5]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://developer.mozilla.org/en-US/docs/Web/HTML
[CSS3]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS3-url]: https://developer.mozilla.org/en-US/docs/Web/CSS
[JavaScript]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[Lambda]: https://img.shields.io/badge/AWS%20Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white
[Lambda-url]: https://aws.amazon.com/lambda/
[APIGateway]: https://img.shields.io/badge/AWS%20API%20Gateway-FF4F00?style=for-the-badge&logo=amazonapigateway&logoColor=white
[APIGateway-url]: https://aws.amazon.com/api-gateway/
[Polly]: https://img.shields.io/badge/AWS%20Polly-232F3E?style=for-the-badge&logo=amazon&logoColor=white
[Polly-url]: https://aws.amazon.com/polly/
[S3]: https://img.shields.io/badge/AWS%20S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white
[S3-url]: https://aws.amazon.com/s3/
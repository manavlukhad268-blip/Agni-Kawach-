# Agni Kawach - System Architecture

```text
[ User / Gallery Image Upload ] 
               │
               ▼
   [ Bolt.new Frontend Interface ]
               │
               ▼
    [ OpenCV Frame Processing ]
               │
               ▼
[ AI Detection Logic (Safe vs Unsafe Fire) ]
               │
       ┌───────┴───────┐
       ▼               ▼
[ Safe (Cooking) ]  [ Unsafe (Hazard/Siren) ]



technical report 

### 2. `TECHNICAL_REPORT.md` फाइल बनाएं
एक और फाइल बनाएं जिसका नाम `TECHNICAL_REPORT.md` रखें और उसमें यह रिपोर्ट डाल दें:

```markdown
# Agni Kawach - Technical Report

## 1. Problem Statement
Traditional fire safety systems often trigger false alarms and fail to distinguish between controlled domestic fires (such as cooking on a stove) and hazardous, unattended fires. "Agni Kawach" is a smart vision system designed to differentiate between safe activities and actual fire hazards.

## 2. Architecture
The system utilizes bolt.new for frontend/UI development and an integrated computer vision and detection logic backend to process image inputs.

## 3. OpenCV Integration
OpenCV is utilized for efficient frame capture, image preprocessing, and visual data handling.

## 4. Implementation
Users upload images or videos via the application interface, which processes the input and instantly evaluates whether the scene is safe or hazardous.

## 5. AWS Deployment
The application is structured for scalable cloud deployment on AWS to ensure fast, reliable, and secure responses.

## 6. Limitations
The current prototype may experience reduced accuracy in extremely complex or low-light environments, which will be optimized in future updates.

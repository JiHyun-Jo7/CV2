# 🎥 Open CV2 
---
### 🤖 개발 환경
- NVIDIA Jetson Nano Development Kit-B01
- Ubuntu 18.04.6 LTS
- python 3.6.9
---
### 01. Open Video
---
- Output mp4 file in samba folder
- samba 폴더에 있는 mp4 파일 출력
---
### 02. Nano Camera 📸
---
- Video Output using CSI, USB camera
- CSI, USB 카메라를 사용하여 영상 출력
---
### 03. RTSP (Real Time Streaming Protocol)
---
- video Output from RTSP 
- RTSP 영상 출력
<details>
	<summary>Threshold Image</summary>
  	<div markdown="1">

![RTSP](https://github.com/JiHyun-Jo7/CV2/assets/141097551/7d444be4-8ea8-4869-8721-efea269eb6b9)


   </div>
</details>

---
### 04. Open Image 🖼️
---
- Position and resize the image to be output
- 이미지를 출력할 위치, 크기 조절
---
### 05. Gray Scale 🐼
---
- Convert Image to Gray
- 이미지를 흑백으로 변환
---
### 06. Get Info 📃
---
- Get Informations in Image
- 이미지의 정보 확인

<details>
	<summary>Information in Image</summary>
  	<div markdown="1">

![info](https://github.com/JiHyun-Jo7/CV2/assets/141097551/0a96bea1-e60f-4663-b705-fe32790533d1)

   </div>
</details>

---
### 07. Draw Polygon ✏️
---
- Draw line, polygons, circle, text
- Select location, Color, Tickness, Size
- 선, 다각형, 원, 텍스트를 입력
- 도형(텍스트)를 입력할 위치, 색상, 두께 선택
---
### 08. Canny 01
---
- Video Edge Detection using Canny
- Canny를 사용한 동영상의 edge 추출
<details>
	<summary>Original</summary>
  	<div markdown="1">

![canny_original](https://github.com/JiHyun-Jo7/CV2/assets/141097551/b3d159f0-d99a-45bc-bb08-482733c34379)

   </div>
</details>
<details>
	<summary>Edge</summary>
  	<div markdown="1">

![canny_edge](https://github.com/JiHyun-Jo7/CV2/assets/141097551/9fcdf70e-35f0-47e8-8582-5ccf38beda69)

   </div>
</details>
<details>
	<summary>Inverse</summary>
  	<div markdown="1">

![canny_inverse](https://github.com/JiHyun-Jo7/CV2/assets/141097551/b1e608e7-cd10-4779-a5a6-f0afeebd339b)

   </div>
</details>

---
### 09. Video Recoding 📹
---
- Recode the Video and Print
- 동영상 녹화 및 출력
---
### 10. Gaussian Blur
---
- Output Gaussian blur in 4 steps
- Display steps as text
- 가우시안 블러 4단계 출력, 단계를 텍스트로 표시

<details>
	<summary>Gaussian Blur</summary>
  	<div markdown="1">

![gaussian01](https://github.com/JiHyun-Jo7/CV2/assets/141097551/e3ec6e02-9fc3-4731-9fa1-70f1f18b23be)
![gaussian02](https://github.com/JiHyun-Jo7/CV2/assets/141097551/d9cd9b06-e312-4e47-9310-23d618721b22)
![gaussian03](https://github.com/JiHyun-Jo7/CV2/assets/141097551/e3069fac-aa2a-474c-a6e8-c39f7901fd94)

   </div>
</details>

---
### 11. Color Palette 🎨
---
- Make color palette using trackbar
- 트랙 바를 사용한 컬러 팔레트
---
### 12. Threshold
---
- Use various thresholds
- 여러 종류의 threshold를 사용

```
cv2.threshold(img, threshold_value, value, flag)
```
|flag|value<th_value|value>th_value|
|:---:|:---:|:---:|
|THRESH_BINARY|0|value|
|THRESH_BINARY_INV|value|0|
|THRESH_TRUNC|img|th_value|
|THRESH_TOZERO|0|img|
|THRESH_TOZERO_INV|img|0|

<details>
	<summary>Threshold Image</summary>
  	<div markdown="1">

![thresholds](https://github.com/JiHyun-Jo7/CV2/assets/141097551/36bcf0ea-7d2b-4ee9-bab2-c434fc54e825)

   </div>
</details>

---
### 13. adaptivethreshold
---
- Use various adaptivethresholds
- 여러 종류의 adaptivethreshold를 사용
---
```
cv2.adaptiveThreshold(img, value, adaptiveMethod, thresholdType, blocksize, C)
```
- img: Grayscale image
- value: adaptiveMethod에 의해 계산된 문턱값과 thresholdType에 의해 픽셀에 적용될 최대값
- adaptiveMethod: 사용할 Adaptive Thresholding 알고리즘
- cv2.ADAPTIVE_THRESH_MEAN_C: 적용할 픽셀 (x,y)를 중심으로 하는 blocksize x blocksize 안에 있는 픽셀값의 평균에서 C를 뺀 값을 문턱값으로 함
- cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 적용할 픽셀 (x,y)를 중심으로 하는 blocksize x blocksize안에 있는 Gaussian 윈도우 기반 가중치들의 합에서 C를 뺀 값을 문턱값으로 함
- blocksize: 픽셀에 적용할 문턱값을 계산하기 위한 블럭 크기. 적용될 픽셀이 블럭의 중심이 됨. 따라서 blocksize는 홀수여야 함
- C: 보정 상수로, 이 값이 양수이면 계산된 adaptive 문턱값에서 빼고, 음수면 더해줌. 0이면 그대로.

<details>
	<summary>Adaptivethreshold Image</summary>
  	<div markdown="1">

![adapt](https://github.com/JiHyun-Jo7/CV2/assets/141097551/0b0877bd-4257-4a36-b825-773ebf8dad55)

   </div>
</details>

---
### 14. Blur 01
---
- Image blurring using pixel average within filter box (5x5)
- 필터 박스(5x5) 안의 픽셀 평균을 사용한 이미지 블러 처리
<details>
	<summary>Blur</summary>
  	<div markdown="1">

![blur01](https://github.com/JiHyun-Jo7/CV2/assets/141097551/82dbf7c8-ceec-47a6-880b-f8a66e918139)


   </div>
</details>

---
### 15. Blur 02
---
- Use 3 different blurring techniques using the trackbar
- 트랙바를 사용하여 3 가지의 블러 처리 기법을 사용
- Blur / Gaussian Blur / MedianBlur
<details>
	<summary>Blur</summary>
  	<div markdown="1">

![blur02_1](https://github.com/JiHyun-Jo7/CV2/assets/141097551/e884bc09-ef68-40dd-818c-e5055e9df89c)
![blur02_2](https://github.com/JiHyun-Jo7/CV2/assets/141097551/6ba41f5c-6f31-4073-b491-97172694b2f3)
![blur02_3](https://github.com/JiHyun-Jo7/CV2/assets/141097551/6e443911-c71b-40a4-a30d-2498359b13b0)

   </div>
</details>

---
### 16. Keyboard ⌨️
---
- Print an embossed image of the keyboard using the Laplacian, Sobel
- Laplacian, Sobel을 사용하여 키보드의 음양각 이미지를 출력
<details>
	<summary>Keyboard</summary>
  	<div markdown="1">

![keyboard](https://github.com/JiHyun-Jo7/CV2/assets/141097551/2708059d-a3f2-4fd4-8989-51fa163f9f3a)

   </div>
</details>

---
### 17. Canny 02 
---
```
edge = cv2.Canny(img, minVal, maxVal)
```
- Image comparison according to minVal, maxVal difference
- minVal, maxVal 값에 따른 이미지 결과 비교
<details>
	<summary>Canny</summary>
  	<div markdown="1">

![canny](https://github.com/JiHyun-Jo7/CV2/assets/141097551/af39d732-9cc1-477e-add3-4117f295df36)

   </div>
</details>

---
### 18. Color Mask
---
- 
- 
<details>
	<summary>title</summary>
  	<div markdown="1">

![colorvideo](https://github.com/JiHyun-Jo7/CV2/assets/141097551/f4496d36-392a-4cd3-bf8b-a7dcfe86579b)

   </div>
</details>

---





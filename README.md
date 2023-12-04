# 🎥 Open CV2 
---
### 🤖 개발 환경
- NVIDIA Jetson Nano Development Kit-B01
- Ubuntu 18.04.6 LTS
- python 3.6.9
---
### 01. [Open Video](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/01_openvideo.py)
---
- Output mp4 file in samba folder
- samba 폴더에 있는 mp4 파일 출력
---
### 02. 📸[Nano Camera](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/02_nanocamera.py)
---
- Video Output using CSI, USB camera
- CSI, USB 카메라를 사용하여 영상 출력
---
### 03. [RTSP (Real Time Streaming Protocol)](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/03_rtsp.py)
---
- video Output from RTSP 
- RTSP 영상 출력
<details>
	<summary>Result</summary>
  	<div markdown="1">

![RTSP](https://github.com/JiHyun-Jo7/CV2/assets/141097551/7d444be4-8ea8-4869-8721-efea269eb6b9)


   </div>
</details>

---
### 04. 🖼️[Open Image](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/04_open_image.py)
---
- Position and resize the image to be output
- 이미지를 출력할 위치, 크기 조절
---
### 05. 🐼[Gray Scale](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/05_grayscale.py)
---
- Convert Image to Gray
- 이미지를 흑백으로 변환
---
### 06. 📃[Get Info](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/06_get_info.py)
---
- Get Informations in Image
- 이미지의 정보 확인

<details>
	<summary>Result</summary>
  	<div markdown="1">

![info](https://github.com/JiHyun-Jo7/CV2/assets/141097551/0a96bea1-e60f-4663-b705-fe32790533d1)

   </div>
</details>

---
### 07. ✏️[Draw Polygon](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/07_draw_polygon.py)
---
- Draw line, polygons, circle, text
- Select location, Color, Tickness, Size
- 선, 다각형, 원, 텍스트를 입력
- 도형(텍스트)를 입력할 위치, 색상, 두께 선택

```
cv2.line(img, (start), (end), Color, thickness)
cv2.rectangle(img, (x, y, ∆x, ∆y), Color, thickness)
cv2.rectangle(img, (start), (end), (0, 155, 0), -1 = fill)
cv2.circle(img, (center), radius, (color), -1)
cv2.polylines(img, [point], True,  Color, thickness)	# point : vertex
cv2.putText(img, text, location, cv2.FONT_HERSHEY_SIMPLEX, Size, Color, thickness)
```
<details>
	<summary>Result</summary>
  	<div markdown="1">

![draw](https://github.com/JiHyun-Jo7/CV2/assets/141097551/769b4e73-8323-497f-a0c7-31aaa57473b3)

   </div>
</details>

---
### 08. [Canny 01](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/08_canny.py)
---
- Video Edge Detection using Canny
- Canny를 사용한 동영상의 edge 추출
<details>
	<summary>Result - Original</summary>
  	<div markdown="1">

![canny_original](https://github.com/JiHyun-Jo7/CV2/assets/141097551/b3d159f0-d99a-45bc-bb08-482733c34379)

   </div>
</details>
<details>
	<summary>Result - Edge</summary>
  	<div markdown="1">

![canny_edge](https://github.com/JiHyun-Jo7/CV2/assets/141097551/9fcdf70e-35f0-47e8-8582-5ccf38beda69)

   </div>
</details>
<details>
	<summary>Result - Inverse</summary>
  	<div markdown="1">

![canny_inverse](https://github.com/JiHyun-Jo7/CV2/assets/141097551/b1e608e7-cd10-4779-a5a6-f0afeebd339b)

   </div>
</details>

---
### 09. 📹[Video Recoding](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/09_video_recoding.py) 
---
- Recode the Video and Print
- 동영상 녹화 및 출력
---
### 10. [Gaussian Blur](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/10_Gaussianblur.py)
---
- Output Gaussian blur in 4 steps
- Display steps as text
- 가우시안 블러 4단계 출력, 단계를 텍스트로 표시

<details>
	<summary>Result</summary>
  	<div markdown="1">

![gaussian01](https://github.com/JiHyun-Jo7/CV2/assets/141097551/e3ec6e02-9fc3-4731-9fa1-70f1f18b23be)
![gaussian02](https://github.com/JiHyun-Jo7/CV2/assets/141097551/d9cd9b06-e312-4e47-9310-23d618721b22)
![gaussian03](https://github.com/JiHyun-Jo7/CV2/assets/141097551/e3069fac-aa2a-474c-a6e8-c39f7901fd94)

   </div>
</details>

---
### 11. 🎨[Color Palette](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/11_color_palette.py)
---
- Make RGB color palette using trackbar
- 트랙 바를 사용한 RGB 컬러 팔레트
<details>
	<summary>Result</summary>
  	<div markdown="1">

![colorpalette_off](https://github.com/JiHyun-Jo7/CV2/assets/141097551/f570cc02-f63d-4dc1-a35a-6e2b183febc0)  
![colorpalette_on](https://github.com/JiHyun-Jo7/CV2/assets/141097551/7ee23a34-4796-45f4-b743-a5943dfb45e7)

   </div>
</details>

---
### 12. [Threshold](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/12_threshold.py)
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
	<summary>Result</summary>
  	<div markdown="1">

![thresholds](https://github.com/JiHyun-Jo7/CV2/assets/141097551/36bcf0ea-7d2b-4ee9-bab2-c434fc54e825)

   </div>
</details>

---
### 13. [Adaptivethreshold](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/13_adaptivethreshold.py)
---
- Use various adaptivethresholds
- 여러 종류의 adaptivethreshold를 사용
---
```
cv2.adaptiveThreshold(img, value, adaptiveMethod, thresholdType, blocksize, C)
```
- img : Grayscale image
- value : adaptiveMethod에 의해 계산된 문턱값과 thresholdType에 의해 픽셀에 적용될 최대값
- adaptiveMethod : 사용할 Adaptive Thresholding 알고리즘
- cv2.ADAPTIVE_THRESH_MEAN_C : 적용할 픽셀 (x,y)를 중심으로 하는 blocksize x blocksize 안에 있는  
				픽셀값의 평균에서 C를 뺀 값을 문턱값으로 함
- cv2.ADAPTIVE_THRESH_GAUSSIAN_C : 적용할 픽셀 (x,y)를 중심으로 하는 blocksize x blocksize안에 있는  
				Gaussian 윈도우 기반 가중치들의 합에서 C를 뺀 값을 문턱값으로 함
- blocksize : 픽셀에 적용할 문턱값을 계산하기 위한 블럭 크기. 적용될 픽셀이 블럭의 중심이 됨.  
	      따라서 blocksize는 홀수여야 함
- C: 보정 상수로, 이 값이 양수이면 계산된 adaptive 문턱값에서 빼고, 음수면 더해줌. 0이면 그대로.

<details>
	<summary>Result</summary>
  	<div markdown="1">

![adapt](https://github.com/JiHyun-Jo7/CV2/assets/141097551/0b0877bd-4257-4a36-b825-773ebf8dad55)

   </div>
</details>

---
### 14. [Blur 01](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/14_blur01.py)
---
- Image blurring using pixel average within filter box (5x5)
- 필터 박스(5x5) 안의 픽셀 평균을 사용한 이미지 블러 처리
<details>
	<summary>Result</summary>
  	<div markdown="1">

![blur01](https://github.com/JiHyun-Jo7/CV2/assets/141097551/82dbf7c8-ceec-47a6-880b-f8a66e918139)


   </div>
</details>

---
### 15. [Blur 02](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/15_blur02.py)
---
- Use 3 different blurring techniques using the trackbar
- 트랙바를 사용하여 3 가지의 블러 처리 기법을 사용
- Blur / Gaussian Blur / MedianBlur
<details>
	<summary>Result</summary>
  	<div markdown="1">

![blur02_1](https://github.com/JiHyun-Jo7/CV2/assets/141097551/e884bc09-ef68-40dd-818c-e5055e9df89c)
![blur02_2](https://github.com/JiHyun-Jo7/CV2/assets/141097551/6ba41f5c-6f31-4073-b491-97172694b2f3)
![blur02_3](https://github.com/JiHyun-Jo7/CV2/assets/141097551/6e443911-c71b-40a4-a30d-2498359b13b0)

   </div>
</details>

---
### 16. ⌨️[Keyboard](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/16_keyboard.py) 
---
- Print an embossed image of the keyboard using the Laplacian, Sobel
- Laplacian, Sobel을 사용하여 키보드의 음양각 이미지를 출력
<details>
	<summary>Result</summary>
  	<div markdown="1">

![keyboard](https://github.com/JiHyun-Jo7/CV2/assets/141097551/2708059d-a3f2-4fd4-8989-51fa163f9f3a)

   </div>
</details>

---
### 17. [Canny 02](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/17_canny02.py)
---
```
edge = cv2.Canny(img, minVal, maxVal)
```
- Image comparison according to minVal, maxVal difference
- minVal, maxVal 값에 따른 이미지 결과 비교
<details>
	<summary>Result</summary>
  	<div markdown="1">

![canny](https://github.com/JiHyun-Jo7/CV2/assets/141097551/af39d732-9cc1-477e-add3-4117f295df36)

   </div>
</details>

---
### 18. [Color Mask](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/18_color_mask.py)
---
- Camera that outputs only a specific range of colors
- 특정 색상만 출력하는 카메라
```
# HSV에서 각 색상을 추출하기 위한 임계값
cv2.inRange(src, lower range, upper range, dst ) 
```
- src : Image, 이미지
- lower range : min of pixel, 픽셀의 최소값
- upper range : max of pixel, 픽셀의 최대값
- dst = None

```
# mask& original image 비트 연산
res = cv2.bitwise_and(img1, img2, mask=mask)
```
- mask 영역에서 공통으로 겹치는 영역 출력

<details>
	<summary>Result</summary>
  	<div markdown="1">

![colorvideo](https://github.com/JiHyun-Jo7/CV2/assets/141097551/f4496d36-392a-4cd3-bf8b-a7dcfe86579b)

```
lower_blue = np.array([110, 100, 100])
upper_blue = np.array([130, 255, 255])

lower_green = np.array([50, 100, 100])
upper_green = np.array([75, 255, 255])

lower_red = np.array([-10, 100, 100])
upper_red = np.array([10, 255, 255])
```
- Unlike the red camera, the green and blue ranges overlap.  
This problem can be solved by adjusting the range of np.array.
- 빨간색 카메라와 달리 초록색과 파란색의 범위가 겹친 것을 확인할 수 있는데,  
이는 np.array의 범위를 조정하면 해결될 것으로 보인다 

   </div>
</details>

---
### 19.
---
-
-


---
### 20. [Match Template](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/20_matchtemplate.py) 
---
- Find different pictures using threshold
- 임계값을 이용한 다른 그림 찾기

<details>
	<summary>Result</summary>
  	<div markdown="1">

![tempmatching](https://github.com/JiHyun-Jo7/CV2/assets/141097551/9990e7ca-1df0-4178-8854-26273fd547a2)

- You can see that one circle that falls below the threshold (0.8) is not displayed.
- 임계값(0.8)에 미달한 원 한개에 박스가 쳐지지 않은 것을 확인할 수 있다

   </div>
</details>

---
### 21. 📖[Teseract](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/21_teseract.py)
---
- Print text in image file
- 이미지 파일 속에 있는 텍스트 출력
<details>
	<summary>Result</summary>
  	<div markdown="1">

![letter02](https://github.com/JiHyun-Jo7/CV2/assets/141097551/12f1d9e1-3f0c-4a3d-8410-7b0d141e5447)
![pytesseract](https://github.com/JiHyun-Jo7/CV2/assets/141097551/4a0813e7-6043-4113-b886-d385bd934405)

   </div>
</details>

---
### 22. [Contour](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/22_contour.py)
---
- Find Outline Using Contour
- 컨투어 기능을 사용하여 아웃라인을 찾는다
<details>
	<summary>Result</summary>
  	<div markdown="1">

![contour](https://github.com/JiHyun-Jo7/CV2/assets/141097551/a5c3cadc-c861-4c99-b9c4-977f36ccd19b)

   </div>
</details>

---
### 23. 🚗[License Plate](https://github.com/JiHyun-Jo7/CV2/blob/144b005e2e03f28916eeb1b66f38238ae2b461f4/23_licenseplate.py) 
---
- Recognizes car license plates in images and outputs data
- 이미지 속 자동차 번호판을 인식하여 데이터를 출력

<details>
	<summary>Result</summary>
  	<div markdown="1">

![licenseplate](https://github.com/JiHyun-Jo7/CV2/assets/141097551/f054a181-1dd9-4211-84f2-5d76d8cfe716)  

![licenseplate_result](https://github.com/JiHyun-Jo7/CV2/assets/141097551/3d079804-126b-4226-9c9f-b585bc502058)
- All letter and numbers matched the result,  
but it was unfortunate that there was a ':' at the end.  
It is assumed that it is because of the '⚡' at the end of the electric vehicle license plate.
- 한글과 숫자 모두 일치했지만 ':' 이 붙는 아쉬운 결과가 나왔다.  
전기차 번호판 끝에 있는 '⚡' 때문이라고 추측된다.

   </div>
</details>
--- 

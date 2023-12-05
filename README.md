# 🎥 Open CV2 
---
### 🤖 개발 환경 (IDE)
- NVIDIA Jetson Nano Development Kit-B01
- Ubuntu 18.04.6 LTS
- python 3.6.9
- lang Kor
---
### 01. [Open Video](01_openvideo.py)
---
- Output mp4 file in samba folder
- samba 폴더에 있는 mp4 파일 출력
---
### 02. 📸[Nano Camera](02_nanocamera.py)
---
- Video Output using CSI, USB camera
- CSI, USB 카메라를 사용하여 영상 출력
---
### 03. [RTSP (Real Time Streaming Protocol)](03_rtsp.py)
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
### 04. 🖼️[Open Image](04_open_image.py)
---
- Position and resize the image to be output
- 이미지를 출력할 위치, 크기 조절
---
### 05. 🐼[Gray Scale](05_grayscale.py)
---
- Convert Image to Gray
- 이미지를 흑백으로 변환
---
### 06. 📃[Get Info](06_get_info.py)
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
### 07. ✏️[Draw Polygon](07_draw_polygon.py)
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
### 08. [Canny 01](08_canny.py)
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
### 09. 📹[Video Recoding](09_video_recoding.py) 
---
- Recode the Video and Print
- 동영상 녹화 및 출력
---
### 10. [Gaussian Blur](10_Gaussianblur.py)
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
### 11. 🎨[Color Palette](11_color_palette.py)
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
### 12. [Threshold](12_threshold.py)
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
### 13. [Adaptivethreshold](13_adaptivethreshold.py)
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
### 14. [Blur 01](14_blur01.py)
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
### 15. [Blur 02](15_blur02.py)
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
### 16. ⌨️[Keyboard](16_keyboard.py) 
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
### 17. [Canny 02](17_canny02.py)
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
### 18. [Color Mask](18_color_mask.py)
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
### 19. [CAM(Continuously Adaptive Mean) Shift](19_camshift.py)
---
- object tracking using camshift
- camshift를 사용한 객체 추적

<details>
	<summary>Result</summary>
  	<div markdown="1">

```
        if k == ord('i'):
            print('Select Area and Enter Key')
            inputmode = True
            frame2 = frame.copy()

            while inputmode:
                cv2.imshow('frame', frame)
                cv2.waitKey(0)
```
- Press 'i' to enter input mode.  
  In input mode, if you draw a rectangle on the desired object with the mouse and press Enter,  
  you can see that the rectangle tracks the object.
- 'i' 를 입력하면 입력모드에 진입한다  
  입력모드에서 마우스로 원하는 객체에 사각형을 그리고 엔터를 입력하면 사각형이 객체를 추적하는 것을 확인할 수 있다

```
        elif event == cv2.EVENT_LBUTTONUP:
            inputmode = False
            rectangle = False
            cv2.rectangle(frame, (col, row), (x, y), (0, 255, 0), 2)
            height, width = abs(row - y), abs(col - x)
            trackWindow = (col, row, width, height)
            roi = frame[row:row+height, col:col+width]
            hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
            roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
            cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
```
- When the left mouse button is released, the input mode and rectangle drawing are terminated  
  The trackWindow variable stores the coordinates and size of the selected region  
  The selected object (ROI) is extracted from the frame, and this ROI is converted to the HSV color space  
  In the HSV space, a mask is applied to select a specific color range, and this is used to calculate the roi_hist, which is then normalized.
- 마우스 왼클릭을 떼면 입력모드와 사각형 그리기가 종료된다  
  trackWindow 변수에 선택한 영역의 좌표와 크기를 저장한다  
  선택한 객체(Roi)를 frame에서 추출하고, 해당 Roi를 HSV 색상 공간으로 변환한다  
  HSV 공간에서 특정 색상 범위를 Masking하여 roi_hist을 계산하고 이 값을 정규화한다

![camshift](https://github.com/JiHyun-Jo7/CV2/assets/141097551/5034351e-0116-4485-be95-2d7a7c9a36a6)

   </div>
</details>

---
### 20. [Mean Shift](20_meanshift.py)
---
- object tracking using meanshift
- meanshift를 사용한 객체 추적  

||When the object blends into the background|Change in size and direction|
|:---:|:---:|:---:|
|CAM|Bad|Good|
|MEAN|Good|Bad|

<details>
	<summary>Result</summary>
  	<div markdown="1">

![meanshift](https://github.com/JiHyun-Jo7/CV2/assets/141097551/fb2c2231-68e6-4e60-a3dc-4f43fc78615d)

   </div>
</details>

---
### 21. 🕵️[Match Template 01](21_matchtemplate01.py) 
---
- Find different pictures using match template
- match template을 이용한 다른 그림 찾기

<details>
	<summary>Result</summary>
  	<div markdown="1">

![tempmatching](https://github.com/JiHyun-Jo7/CV2/assets/141097551/9990e7ca-1df0-4178-8854-26273fd547a2)

- You can see that one circle that falls below the threshold (0.8) is not displayed.
- 임계값(0.8)에 미달한 원 한개에 박스가 쳐지지 않은 것을 확인할 수 있다

- Template Matching의 단점
  - scale(크기)에 민감 : 같은 크기의 sliding window로 템플릿을 매칭시켜가며 찾기 때문에 크기에 민감하다.
    템플릿이나 원본 이미지의 크기를 변형시키며 매칭하는 방법으로 해결해야 한다. --> multi scale template matching
  - rotation(회전)에 민감 : 위와 같은 이유로 회전에 민감하다. 이 또한 회전시켜가며 매칭할 수 있지만, 각도가 조금만 다르면 성능이 떨어진다. 

   </div>
</details>

---
### 22. 🕵️[Match Template 02](20_matchtemplate02.py) 
---
- Use various match templates
- 여러 종류의 match templates 사용해보기

||Matching|Good|Bad|No correlation|
|:---:|:---:|:---:|:---:|:---:|
|cv2.TM_CCOEFF|Correlation coefficient|1|-1|0|
|cv2.TM_CCOEFF_NORMED|CCOEFF Normalization|-|-|-|
|cv2.TM_CCORR|Correlation relationship|↑|0|-|
|cv2.TM_CCORR_NORMED|CCORR Normalization|-|-|-|
|cv2.TM_SQDIFF|Squared difference|0|↑|-|
|cv2.TM_SQDIFF_NORMED|SQDIFF Normalization|-|-|-|

<details>
	<summary>Result</summary>
  	<div markdown="1">

![matchtemplate01](https://github.com/JiHyun-Jo7/CV2/assets/141097551/c572a610-d483-43df-80fe-28942d5833b8)
![matchtemplate02](https://github.com/JiHyun-Jo7/CV2/assets/141097551/8e3bcd09-f0a8-4e8e-8180-970795fa7b3b)
![matchtemplate03](https://github.com/JiHyun-Jo7/CV2/assets/141097551/3d2f2677-b619-4282-bbee-46f9f4d09caa)
![matchtemplate04](https://github.com/JiHyun-Jo7/CV2/assets/141097551/7057b295-f948-40c7-ae30-3b2afb89775f)
![matchtemplate05](https://github.com/JiHyun-Jo7/CV2/assets/141097551/56d720b3-6d41-4b0b-9f87-133424cc9f5e)


   </div>
</details>

---
### 23. [Contour](23_contour.py)
---
- Create image contour lines. The recognition rate of objects is high when the background is black and the object is white.
- 이미지 등고선을 만든다 찾을 객체를 하얀색, 배경을 검은색으로 만들면 객체 인식률이 높아진다

```
cv2.findContours(thimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```
- cv2.RETR_external	가장 바깥쪽의 외곽선만 찾음
- cv2.RETR_list		모든 외곽선을 찾지만 계층 구조를 구성하지 않음
- cv2.RETR_ccomp	모든 외곽선을 찾고 2레벨의 계층 구조로 구성
- cv2.RETR_tree		모든 외곽선을 찾고 모든 계층 구조를 구성
  
<details>
	<summary>Result</summary>
  	<div markdown="1">

![contour](https://github.com/JiHyun-Jo7/CV2/assets/141097551/a5c3cadc-c861-4c99-b9c4-977f36ccd19b)

   </div>
</details>

---
### 24. 📖[Teseract](24_teseract.py)
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
### 25. 🚗[License Plate](25_licenseplate.py) 
---
- Recognize car license plates in images using Open CV, preprocess data, and output processed data with tesseract
- Open CV를 사용하여 이미지 속 자동차 번호판을 인식하여 데이터를 가공, tesseract로 가공한 데이터 출력

<details>
	<summary>Result</summary>
  	<div markdown="1">

```
# Convert image to black and white and Outline extraction
edge = cv2.Canny(dst, 150, 180)
cv2.imshow('edge', edge)
```
- White letters on a black background are important for high recognition rates.  
Black and white processing was performed using Canny instead of Threshold.
- It was more effective than Threshold as it removed noise that could not be removed with Gaussian Blur.
- 높은 인식률을 얻기 위해서는 검정 배경에 흰 글자로 만드는 것이 중요하다  
Threshold 대신 Canny를 사용하여 흑백 처리를 진행했다
- Gaussian Blur 로 제거되지 않았던 잡음이 함께 제거되어  Threshold 보다 더 효과적이었다
		
![licenseplate](https://github.com/JiHyun-Jo7/CV2/assets/141097551/7f1dc02f-863a-4332-af51-69367ec0e9b3)
![licenseplate_result](https://github.com/JiHyun-Jo7/CV2/assets/141097551/8bb21b28-7c56-4b09-b779-8f3ddf30b417)

- The number of car numbers in Korea has been reorganized several times recently, so the number is not unified.  
  If the number of numbers is unified in a country, it would be good to use the <config='--psm x'> function. (x = number of license plate)
- If i use the YOLO module, you can automatically recognize the location of the car license plate,  
  but it is a bit disappointing that it was not applied.
- 한국의 자동차 번호의 수는 최근 수차례 개편되어 갯수가 통일되어있지 않은데,  
  만일 번호의 수가 통일되어있는 국가라면 <config='--psm x'> 기능을 사용하면 좋을 것 같다 (x = 자동차 번호의 수)
- YOLO 모듈을 사용하면 자동차 번호판을 자동으로 인식할 수 있는데 해당 기능을 적용하면 더 좋은 프로그램이 될 것 같다

   </div>
</details>
--- 

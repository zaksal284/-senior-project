import cv2,sys,datetime,os #blackbox
from PIL import ImageFont #blackbox
import deletefile

#------------------------------------------------- 비디오 녹화 및 저장시작-------------------------------------
def cctv(start):
#-------------------------------------------------초기설정----------------------------------------------------------

   Video=cv2.VideoCapture(0)
   Time = datetime.datetime.now()
   VideoFileName = Time.strftime('%Y-%m-%d_%H-%M-%S') + '.avi'      # 파일이름= 년 원 일 시 분 초.avi
   w = round(Video.get(cv2.CAP_PROP_FRAME_WIDTH))                   # width  해상도결정
   h = round(Video.get(cv2.CAP_PROP_FRAME_HEIGHT))                  # height 해상도결정
   if not Video.isOpened():
    print("비디오 소스를 열 수 없습니다.")
   fps = Video.get(cv2.CAP_PROP_FPS)                                # 초당프레임 설정->재생속도설정
   fourcc = cv2.VideoWriter_fourcc(*'DIVX')                         # 코덱결정
   delay = round(1000/fps)
   font = ImageFont.truetype("/home/keepboard/Desktop/fonts/SCDream6.otf", 20) #폰트설정
#-------------------------------------------------초기설정 끝-----------------------------------------------

#------------------------------------------------비디오 저장설정--------------------------------------------
   deletefile.deletefile()
   Video_Path = os.path.join("/home/keepboard/Desktop/blackbox", VideoFileName)# 비디오 저장장소~
   out = cv2.VideoWriter(Video_Path, fourcc, fps, (w,h)) #위치,코덱,주파수,해상도로 저장
   if not (out.isOpened()): # 만약에 out이 만들어 지지 않았다면
      print("File isn't opend!!")
      Video.release() #비디오닫기
      sys.exit()
#--------------------------------------------------비디오 설정끝------------~--------------------------------
   while True:
      ret, frame = Video.read() #비디오를 읽어옴
      if ret:
         inversed = cv2.flip(frame, 1) #flip을 이용해서 좌우반전
   
      #시간
      Time = datetime.datetime.now() #현재시간
      nowDatetime = Time.strftime("%Y/%m/%d, %H:%M:%S") #년/월/일, 시:분:초
      cv2.putText(inversed, nowDatetime, (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA) #텍스트출력
      out.write(inversed) #영상 저장
      if start.value==False:
         Video.release()
         out.release()
         break

#------------------------------------------------------black box 종료-------------------------------------


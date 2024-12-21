import serial
import csv
import time

# 시리얼 포트 설정
serial_port = "COM3"  # Windows: COM포트 번호, macOS/Linux: "/dev/ttyUSB0"와 유사
baud_rate = 9600
output_file = "gsr_data.csv"

# 시리얼 포트 열기
ser = serial.Serial(serial_port, baud_rate)
print(f"Connected to {serial_port} at {baud_rate} baud")

# CSV 파일 열기
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp(ms)", "GSR_Average"])  # 헤더 작성

    try:
        while True:
            # 시리얼 데이터 읽기
            if ser.in_waiting > 0:
                line = ser.readline().decode("utf-8").strip()  # 한 줄 읽기
                print(line)  # 출력 확인

                # 데이터를 CSV에 저장
                data = line.split(",")
                if len(data) == 2:  # 데이터가 올바른 형식인지 확인
                    writer.writerow(data)

    except KeyboardInterrupt:
        print("데이터 저장 종료")

# 시리얼 포트 닫기
ser.close()

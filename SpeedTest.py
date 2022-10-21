import speedtest

test = speedtest.Speedtest(secure = true)

down_speed = test_download()
up_speed = test_upload()

print('Dowonload Speed: ', down_speed)
print('Upload Speed', up_speed)


class Config(object):
    
    #file path 
    data_path_aions = "../chen_data/car_august/aions_august/" #where aions raw data was saved
    data_path_gs3 = "../chen_data/car_august/gu3_august/" #where gs3 raw data was saved
    data_path_gs4 = "../chen_data/car_august/gs4_august/" #where gs4 raw data was saved
    
    #header
    header_path_gs3 = "gs3_head.txt"
    header_path_gs4 = "gs4_head.txt"
    header_path_aions = "aions_head.txt"
    
    #前処理のパラメータparameter
    therhold_accl = 0.3 * 9.8#急加速度、急減速度の閾値は０．３G
    skip_step = 5 #5秒以内に同じイベントを発生してもカウントしない
    time_diff = 2 #時間差3秒以降のデータは同じイベントとしてカウントしない
    
    
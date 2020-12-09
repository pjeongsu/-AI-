from service import create_app

app = create_app()

# 서버가동
if __name__ == '__main__':
    host = '127.0.0.1' # real : '0.0.0.0'
    port = 5000        # real : 기타포트 or 80
    debug = True       # real : False
    # 환경변수에 의해서 값들이 변경되어, 서버가동이 가능
    if app.config['IS_REAL']: # 실환경
        host = app.config['REAL_SVR_URL']
        port = app.config['REAL_SVR_PORT']
    else: # 테스트 환경
        host = app.config['TEST_SVR_URL']
        port = app.config['TEST_SVR_PORT']

    # 서버가동
    app.run(host = host,
            port = port,
            debug= debug)
import speedtest
servername =[]

try:
    st1 =speedtest.Speedtest()

    print(f"upload speed {st1.upload()}")

    print(f"Download speed {st1.download()}")


    print(f"ping speed {st1.get_servers(servername)}")
except speedtest.ConfigRetrievalError:
    print("Timeout Buddy Please Try Again Later")
    pass
except KeyboardInterrupt:
    pass
except speedtest.SpeedtestException:
    pass
except speedtest.AbstractHTTPHandler:
    pass
except speedtest.FakeSocket:
    pass

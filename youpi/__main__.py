from youpi import YouTube

if __name__=='__main__':
    yt = YouTube('EWKtTo4MYrg')
    
    yt_streams = yt.streams
    best = yt_streams.best_both()
    print(best)
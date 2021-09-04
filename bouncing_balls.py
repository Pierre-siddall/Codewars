def bouncing_ball(h, bounce, window):
    if h>0 and 0<bounce<1 and window<h:
        count=0
        while h*bounce>window:
            count+=1
            h=h*bounce
        return (count*2)+1
    else:
        return -1
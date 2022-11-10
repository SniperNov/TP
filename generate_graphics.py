# %matplotlib inline
from brokenaxes import brokenaxes as bkx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def loop1_schedule():
    loop1_static = [1.726990,1.630944,1.634503,1.660471,1.661041,1.769077,1.831959]
    loop1_guided = [1.680981,1.571464,1.581789,1.605133,1.625474,1.683612,1.843258]
    loop1_dynamic = [1.729001,1.633339,1.593980,1.606236,1.637933,1.728000,1.852333]
    loop1_static_ns = 3.151056
    loop1_auto = 1.711301
    loop1_before = [10.973513]
    x_fault = [0,1,2,3,4,5,6]
    # x_data = [1,2,4,8,16,32,64]
    xaxis = ['1','2','4','8','16','32','64']
    xaxis2 = ['NaN']
    xlabel = 'Chunksize'
    ylabel = 'runtime (sec)'
    data=[loop1_static, loop1_dynamic, loop1_guided]
    fig = plt.figure(figsize=(16,9))
    bax = bkx(ylims=((1.55,1.88),(3.14,3.16)),hspace = 0.05)
    bax.plot(xaxis,loop1_static, mcolors.CSS4_COLORS['darksalmon'],marker='*',label='Static_n')
    bax.plot(xaxis,loop1_dynamic, mcolors.CSS4_COLORS['darkseagreen'],marker='*',label='Dynamic_n')
    bax.plot(xaxis,loop1_guided, mcolors.CSS4_COLORS['goldenrod'],marker='*',label='Guided_n')
    # bax.plot(x_data,loop1_auto, mcolors.CSS4_COLORS['darkseagreen'],marker='*',label='Auto')
    # bax.plot(x_data,loop1_static_ns,mcolors.CSS4_COLORS['darkslategray'],marker='*',label='Static')
    bax.axhline(loop1_auto, color=mcolors.CSS4_COLORS['darkslategray'], ls='dotted',label='Auto')
    bax.axhline(loop1_static_ns, color=mcolors.CSS4_COLORS['indianred'], ls='dotted',label='Static')

    plt.title('Loop 1',fontsize=10)
    bax.set_xlabel(xlabel,fontsize=10)
    bax.set_ylabel(ylabel,fontsize=10)
    bax.grid(axis='both', which='major', ls='-',alpha=0.2)
    for a, b in zip(x_fault, loop1_static):
        bax.text(a, b, '%.3f'%b, ha='right', va='top', fontsize=8,rotation=-45)
    for a, b in zip(x_fault, loop1_dynamic):
        bax.text(a, b, '%.3f'%b, ha='left', va='bottom', fontsize=8,rotation=-45)
    for a, b in zip(x_fault, loop1_guided):
        bax.text(a, b, '%.3f'%b, ha='right', va='top', fontsize=8,rotation=-45)
    bax.text(6, loop1_auto, '%.3f'%loop1_auto, ha='center', va='bottom', fontsize=8,rotation=-45)
    bax.text(6, loop1_static_ns, '%.3f'%loop1_static_ns, ha='center', va='bottom', fontsize=8,rotation=-45)
    bax.legend(loc='lower right')
    plt.show()

def loop2_schedule():
    loop2_static = [3.511922,2.551646,2.252989,2.467286,2.468031,3.968808,7.262355]
    loop2_guided = [9.531336,9.450048,9.424558,9.432902,9.425920,9.471262,9.504044]
    loop2_dynamic = [1.884593,1.869117,1.856366,1.860541,1.862710,3.605009,6.919342]
    loop2_static_ns = [10.313997]
    loop2_auto = [8.434092]
    loop2_before = 12.701866
    x_fault = [0,1,2,3,4,5,6]
    xaxis = ['1','2','4','8','16','32','64']
    xaxis2 = ['NaN']
    originalaxis = [0,1,2,3,4,5,6]
    fig = plt.figure(figsize=(16,9))
    bax = bkx()
    
    bax.plot(xaxis,loop2_static, mcolors.CSS4_COLORS['darksalmon'],marker='*',label='Static_n')
    bax.plot(xaxis,loop2_dynamic, mcolors.CSS4_COLORS['darkseagreen'],marker='*',label='Dynamic_n')
    bax.plot(xaxis,loop2_guided, mcolors.CSS4_COLORS['goldenrod'],marker='*',label='Guided_n')

    bax.axhline(loop2_auto, color=mcolors.CSS4_COLORS['darkslategray'], ls='dotted',label='Auto')
    bax.axhline(loop2_static_ns, color=mcolors.CSS4_COLORS['indianred'], ls='dotted',label='Static')

    plt.title('Loop 2',fontsize=10)
    bax.set_xlabel('Chunksize',fontsize=10)
    bax.set_ylabel('runtime (sec)',fontsize=10)
    bax.grid(axis='both', which='major', ls='-',alpha=0.2)
    for a, b in zip(x_fault, loop2_static):
        bax.text(a, b, '%.3f'%b, ha='center', va='bottom', fontsize=8,rotation=-45)
    for a, b in zip(x_fault, loop2_dynamic):
        bax.text(a, b, '%.3f'%b, ha='center', va='bottom', fontsize=8,rotation=-45)
    for a, b in zip(x_fault, loop2_guided):
        bax.text(a, b, '%.3f'%b, ha='center', va='bottom', fontsize=8,rotation=-45)
    bax.text(6, loop2_auto[0], '%.3f'%loop2_auto[0], ha='center', va='bottom', fontsize=8,rotation=-45)
    bax.text(6, loop2_static_ns[0], '%.3f'%loop2_static_ns[0], ha='center', va='bottom', fontsize=8,rotation=-45)
    bax.legend(loc='lower right')
    plt.show()

def printloop1sp():
    loop1_guided = [11.827717,5.522716,2.957461,2.152060,1.677219,1.156778,0.889412,0.731583,0.689459]
    loop1_before = 10.973513
    sp = [loop1_before/x for x in loop1_guided]

    print(sp)
    test_thread = [1,2,4,6,8,12,16,24,32]

    xaxis = ['1','2','4','8','16','32','64']
    xlabel = 'Number of Threads'
    ylabel = 'Speedup Ts/Tp'
    fig = plt.figure(figsize=(16,9))
    plt.plot(test_thread,sp, mcolors.CSS4_COLORS['indianred'],marker='*',label='Guided,2')

    plt.title('Loop 1 Speedup',fontsize=10)
    plt.xlabel(xlabel,fontsize=10)
    plt.ylabel(ylabel,fontsize=10)
    plt.grid(axis='both', which='major', ls='-',alpha=0.2)
    plt.xticks(np.arange(0, 35, 1.0))
    for a, b in zip(test_thread, sp):
        plt.text(a, b, '%.3f'%b, ha='center', va='bottom', fontsize=10,rotation=0)

    plt.legend(loc='lower right')
    plt.show()

def printloop2sp():
    loop2_dynamic = [13.531995,6.534977,3.455024,2.449527,1.889679,1.352439,0.996909,0.882399,0.886900]
    loop2_before = 12.701866
    sp = [loop2_before/x for x in loop2_dynamic]

    print(sp)
    test_thread = [1,2,4,6,8,12,16,24,32]

    xaxis = ['1','2','4','8','16','32','64']
    xlabel = 'Number of Threads'
    ylabel = 'Speedup Ts/Tp'
    fig = plt.figure(figsize=(16,9))
    plt.plot(test_thread,sp, mcolors.CSS4_COLORS['indianred'],marker='*',label='Dynamic,8')

    plt.title('Loop 2 Speedup',fontsize=10)
    plt.xlabel(xlabel,fontsize=10)
    plt.ylabel(ylabel,fontsize=10)
    plt.grid(axis='both', which='major', ls='-',alpha=0.2)
    plt.xticks(np.arange(0, 35, 1.0))
    for a, b in zip(test_thread, sp):
        plt.text(a, b, '%.3f'%b, ha='center', va='bottom', fontsize=10,rotation=0)

    plt.legend(loc='lower right')
    plt.show()

loop1_schedule()
loop2_schedule()
printloop1sp()
printloop2sp()
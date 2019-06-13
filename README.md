# IGRF
计算地球非偶极子场

## CONTENTS

- [数据](#数据)
- [公式](#公式)
- [结果](#结果)
- [代码](#代码)

## 数据

数据来自 [International Geomagnetic Reference Field](https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html)

txt格式数据文件[下载](https://www.ngdc.noaa.gov/IAGA/vmod/coeffs/igrf12coeffs.txt)

excel格式数据文件[下载](https://www.ngdc.noaa.gov/IAGA/vmod/coeffs/IGRF12coeffs.xls)



将txt文件的前四行删掉

## 公式

公式如下：
$$
V(r, \theta, \phi, t)=a \sum_{n=1}^{N} \sum_{m=0}^{n}\left(\frac{a}{r}\right)^{n+1}\left[g_{n}^{m}(t) \cos (m \phi)+h_{n}^{m}(t) \sin (m \phi)\right] P_{n}^{m}(\cos \theta)
$$

我们只计算它的Z分量，公式如下：
$$
V(r, \theta, \phi, t)=-(n+1) \sum_{n=1}^{N} \sum_{m=0}^{n}\left(\frac{a}{r}\right)^{n+2}\left[g_{n}^{m}(t) \cos (m \phi)+h_{n}^{m}(t) \sin (m \phi)\right] P_{n}^{m}(\cos \theta)
$$

其中 a 为地球半径，我们只计算地表的，即 $r = a$.

$P_{n}^{m}(\cos \theta)$ 是半归一化的连带勒让德函数，而python中的`scipy.special.lpmv()`函数是完全没有归一化的，我们需要将其归一化，可用以下公式:
$$
\begin{array}{l}{P_{n}(x) \text { for } m=0} \\ {s_{n}^{m}(x)=(-1)^{m} \sqrt{\frac{2(n-m) !}{(n+m) !}} P_{n}^{m}(x) \text { for } m>0}\end{array}
$$

## 结果

将所得结果放置在pngfile目录下，共25张，还有一张gif动图(IGRF.gif)在主目录下.

## 代码

igrfcode.py

constant.py

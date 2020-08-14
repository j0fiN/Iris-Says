import plotly.express as px

data_frame = px.data.iris()


def scatter(to_html=False):
    fig_pw_pl = px.scatter(data_frame, x="petal_width", y="petal_length", color="species")
    fig_pw_sw = px.scatter(data_frame, x="petal_width", y="sepal_width", color="species")
    fig_pw_sl = px.scatter(data_frame, x="petal_width", y="sepal_length", color="species")

    fig_pl_pw = px.scatter(data_frame, x="petal_length", y="petal_width", color="species")
    fig_pl_sw = px.scatter(data_frame, x="petal_length", y="sepal_width", color="species")
    fig_pl_sl = px.scatter(data_frame, x="petal_length", y="sepal_length", color="species")

    fig_sw_pw = px.scatter(data_frame, x="sepal_width", y="petal_width", color="species")
    fig_sw_pl = px.scatter(data_frame, x="sepal_width", y="petal_length", color="species")
    fig_sw_sl = px.scatter(data_frame, x="sepal_width", y="sepal_length", color="species")

    fig_sl_pw = px.scatter(data_frame, x="sepal_length", y="petal_width", color="species")
    fig_sl_pl = px.scatter(data_frame, x="sepal_length", y="petal_length", color="species")
    fig_sl_sw = px.scatter(data_frame, x="sepal_length", y="sepal_width", color="species")

    fig_3d = px.scatter_3d(data_frame, x='sepal_length', y='sepal_width', z='petal_width',
                           symbol='species', color='petal_length', labels=None, color_continuous_scale='ice')

    if to_html is False:
        return "Done"
    else:
        fig_pw_pl.write_html("static/graphs/fig_pw_pl.html")
        fig_pw_sw.write_html("static/graphs/fig_pw_sw.html")
        fig_pw_sl.write_html("static/graphs/fig_pw_sl.html")

        fig_pl_pw.write_html("static/graphs/fig_pl_pw.html")
        fig_pl_sw.write_html("static/graphs/fig_pl_sw.html")
        fig_pl_sl.write_html("static/graphs/fig_pl_sl.html")

        fig_sw_pw.write_html("static/graphs/fig_sw_pw.html")
        fig_sw_pl.write_html("static/graphs/fig_sw_pl.html")
        fig_sw_sl.write_html("static/graphs/fig_sw_sl.html")

        fig_sl_pw.write_html("static/graphs/fig_sl_pw.html")
        fig_sl_pl.write_html("static/graphs/fig_sl_pl.html")
        fig_sl_sw.write_html("static/graphs/fig_sl_sw.html")

        fig_3d.write_html("static/graphs/fig_3d.html")
        return "Done Saving"


if __name__ == '__main__':
    pass
    # scatter()

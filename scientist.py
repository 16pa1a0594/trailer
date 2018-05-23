#!/usr/bin/env python
import webbrowser
import os
import re

main_page_head = '''
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scientists</title>

    <script src="https://code.jquery.com/jquery-1.12.3.min.js" integrity="sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
        crossorigin="anonymous"></script>
        <link href="https://fonts.googleapis.com/css?family=Courgette" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function () {
            $("#myVideo").on("hidden.bs.modal", function () {
                $("#myframeX").attr("src", "#");
            })
        })
        function changeVideo(vId) {
            var iframe = document.getElementById("myframeY");
            iframe.src = "https://www.youtube.com/embed/" + vId;
            $("#myVideo").modal("show");
        }
    </script>
    <style>
        .container {
            flex-wrap: wrap;
            display: flex;
            flex: 20%;
            justify-content: center;
            
        }
        body {
            margin: 0;
        }
        
        header {
            color: rgb(0,128,128);
            text-align: center;
            font-size: 60px;
        }
        img{
            height: 450px;
            width: 450px;
        }
		
           .img1:hover,
           .img2:hover,
           .img3:hover,
           .img4:hover{
            background-color: rgb(0,128,128);
     
           }

        .img1{

            padding-top: 30px;
            padding-left: 30px;
            padding-bottom: 30px;
            padding-right: 30px;
            background-color: rgb(128,128,128);
            border-radius: 10px;
            margin-bottom:30px;
            margin-top: 30px;
            margin-left: 40px;

        }
        .img2 {
            padding-top: 30px;
            padding-left: 30px;
            padding-bottom: 30px;
            padding-right: 30px;
            background-color: rgb(128,128,128);
            border-radius: 10px;
            margin-bottom:30px;
            margin-top: 30px;
            margin-left: 40px;


        }
        .img3 {
            padding-top: 30px;
            padding-left: 30px;
            padding-bottom: 30px;
            padding-right: 30px;
            background-color: rgb(128,128,128);
            border-radius: 10px;
            margin-bottom:30px;   
            margin-top: 30px;
            margin-left: 40px;


        }
        .img4 {
            padding-top: 30px;
            padding-left: 30px;
            padding-bottom: 30px;
            padding-right: 30px;
            background-color: rgb(128,128,128);
            border-radius: 10px;
            margin-bottom:30px;
            margin-top: 30px;
            margin-left: 40px;


        }
        
    </style>
    </head>'''


main_page_content ='''<body>
    <header></i> Scientists </i></header><br><br>
    <main>
        <div class="container">
            <div class="img1" onclick="changeVideo('ZAGY36JYQlg')">
                <img  src="http://www.sciencekids.co.nz/images/pictures/scientists/alexandergrahambell.jpg" alt="alexander"width: 450 height:450>
                <figcaption>Alexander</figcaption>
            </div>
            <div class="img2" onclick="changeVideo('HQ2RJC1a8T0')">
                <img src="https://cdn-images-1.medium.com/max/1186/1*s2GyMoLeSV3Epc2Gk3qBXA.png" alt="thomas"width: 450 height: 450">
                <figcaption>Thomas</figcaption>
            </div>
            <div class="img3" onclick="changeVideo('Rejbk1oJ2xg')">
                <img src="https://media5.picsearch.com/is?u3DTOHIfghifvYGbeRkN9yWBWfjsQG74NlDirr81ppM&height=289" alt="galileo"width: 450 height: 450">
                <figcaption>Galileo</figcaption>
            </div>
            <div class="img4" onclick="changeVideo('aiGxZGXB7lE')">
               <img src="https://media3.picsearch.com/is?gudYY5Mvkgd2r59dZ9eTqdE_pULpiupnsSPiTvJS7-o&height=341" alt="schrodinger"width: 450 height: 450">
                <figcaption>Schrodinger</figcaption>
            </div>   
        
        <div class="modal fade" id="myVideo" tabindex="0" role="history" aria-labelledby="myModalLabel">
            <div class="modal-dialog" role="history">
                <div class="modal-content">
                    <div class="modal-body">
                        <iframe id="myframeY" width="572" height="372" src="" frameborder="0" allowfullscreen></iframe>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal"><b>X</b></button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>

</html>'''


movie_title_content = ''' 
<div class ="modal fade" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-transfer="#trailer">
    <img src="{poster_image_url}" width=220 height = "342">
    <h2 style="color:white;">{movie_title}</h2>
</div>
'''
def create_movie_title_content(movies):
	content = ''
	for movie in movies:
		youtube_id_match = re.search(r'(?<=v=)[^&#]+',movie.trailer_youtube_url)
		youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',movie.trailer_youtube_url)
		trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)
		content+=movie_title_content.format(movie_title = movie.title,poster_image_url = movie.poster_image_url,trailer_youtube_id = movie.trailer_youtube_url)
	return content
def open_movies_page(movies):
	#create or overwrite the output file
	output_file = open('mve_trailer.html','w')
	#replace the movie titles placeholder generated content
	rendered_content = main_page_content.format(movie_titles = create_movie_title_content(movies))
	#output the file
	output_file.write(main_page_head + rendered_content)
	output_file.close()
	#open the output file in the browser(in a new tab,if possible)
	url = os.path.abspath(output_file.name)
	webbrowser.open('file://'+url,new=2)
	

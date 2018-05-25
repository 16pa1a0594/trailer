#!usr/bin/env python
import media
import scientist
alexander = media.Movie("Alexander",
                        "https://cdn-images-1.medium.com/max/1186/1*s2GyMoLe"
                        "SV3Epc2Gk3qBXA.png ",
                        "https://www.youtube.com/embed/ZAGY36JYQlg ")
thomas = media.Movie("Thomas",
                     "https://media5.picsearch.com/is?u3DTOHIfghifvYGbeRkN9"
                     "yWBWfjsQG74NlDirr81ppM&height=289",
                     "https://www.youtube.com/embed/HQ2RJC1a8T0")
galileo = media.Movie("Galileo",
                      "https://media3.picsearch.com/is?gudYY5Mvkgd2r59dZ9eT"
                      "qdE_pULpiupnsSPiTvJS7-o&height=341",
                      "https://www.youtube.com/embed/Rejbk1oJ2xg")
schrodinger = media.Movie("Schrodinger",
                          "https://media3.picsearch.com/is?gudYY5Mvkgd2r59d"
                          "Z9eTqdE_pULpiupnsSPiTvJS7-o&height=341",
                          "https://www.youtube.com/embed/aiGxZGXB7lE")
Movies = [alexander, thomas, galileo, schrodinger]
scientist.open_movies_page(Movies)


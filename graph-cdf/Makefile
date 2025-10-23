PLT_FILES := $(wildcard *.plt)
PDF_FILES := $(wildcard *.pdf)

all: clean plot eps
eps: $(PDF_FILES:.pdf=.eps)
plot: $(PLT_FILES:.plt=.pdf)
clean:
	rm -f eps/*.eps

%.pdf: %.plt
	gnuplot $<

%.eps: %.pdf
	pdf2ps $< eps/$@

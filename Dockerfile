FROM python:slim AS build
WORKDIR /app
COPY app.py .

FROM python:slim AS runtime
WORKDIR /app
COPY --from=build /app/app.py .

ENTRYPOINT ["python", "app.py"]
CMD []
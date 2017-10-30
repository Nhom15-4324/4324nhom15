![Các hệ thống phân tán](https://user-images.githubusercontent.com/26924023/32180538-d4a9693e-bdc4-11e7-89d7-a3d31299c1fe.png)
## Bài tập nhóm Môn học Các hệ thống phân tán &nbsp;

## Các phần mềm cần thiết &nbsp;
- [Xampp](https://www.apachefriends.org/index.html)
- [Eclipse IDE for Java Developers](https://www.eclipse.org/downloads/packages/eclipse-ide-java-developers/keplersr1)
- [Flyway and Maven Plugin](https://flywaydb.org/getstarted/download)

## Tìm hiểu về Flyway

**Flyway là gì!?**
```sh
Flyway là một java open source library hỗ trợ migrate data cho các ứng dụng, một khi chúng ta cần:
- Nâng cấp database khi thay đổi cấu trúc hoặc dữ liệu.
- Quản lý lịch sử thay đổi version một cách chặt chẽ.
- Thực thi migrating một cách tự động.
- Đồng bộ data structure giữa các server development.
Hỗ trợ hầu hết các relational database:


```
![List Relational Database](https://user-images.githubusercontent.com/26924023/32181111-320d68f4-bdc6-11e7-88e6-b32d6edc1ed9.png)

**Flyway hoạt động như thế nào**
```sh
Flyway tạo ra một table có tên SCHEMA_VERSION dùng để quản lý lịch sử phiên bản cũng như trạng thái của database.

```
![Database changed](https://user-images.githubusercontent.com/26924023/32181124-39ed717c-bdc6-11e7-8692-993587be48f3.png)

## Tích hợp Flyway Maven Plugin

**Tạo maven project:**
```sh
# Tạo java console app sử dụng maven từ command line hoặc IDE:

mvn archetype:generate -B \
        -DarchetypeGroupId=org.apache.maven.archetypes \
        -DarchetypeArtifactId=maven-archetype-quickstart \
        -DarchetypeVersion=1.1 \
        -DgroupId=flyway-maven-sample \
        -DartifactId=flyway-maven-sample \
        -Dversion=1.0-SNAPSHOT \
        -Dpackage=manhnv.flyway.sample

```
**Add Jdbc Driver Dependency:**
```sh
# Thêm Dependencies vào file Pom.xml
<dependencies>
        <!--Add postgres jdbc driver-->
        <dependency>
            <groupId>postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <version>9.1-901.jdbc4</version>
        </dependency>
    </dependencies>
```


## Tài liệu tham khảo online
- [Migration data với Flyway sử dụng Maven](https://blog.udemy.com/xampp-tutorial/): Giới thiệu về Flyway và cách sử dụng flyway với Maven.
- [How to integrate Flyway on Maven](https://www.youtube.com/watch?v=lx-OAJKFDBg): Cách tích hợp Maven với Flyway.


## Phân chia thực hiện
Cả nhóm cùng thự hiện nghiên cứu Flyway trong giai đoạn 1.

## Nhóm
Danh sách nhóm sinh viên thực hiện:

[![Trần Lục Long Tính](https://user-images.githubusercontent.com/26924023/32182362-0f664dfe-bdc9-11e7-87e6-8ec55ea5213e.jpg)](https://www.facebook.com/tinh.dk) |  [![Hoàng Công Kiên](https://user-images.githubusercontent.com/26924023/32182367-131334d0-bdc9-11e7-96e5-0d6e7ee5e949.png)](https://www.facebook.com/hck1996)| [![Huỳnh Vân Nhật](https://user-images.githubusercontent.com/26924023/32182372-15090cb0-bdc9-11e7-8aa4-efc3a7421227.png)](https://www.facebook.com/hvn96) | [![Trần Văn Dân](https://user-images.githubusercontent.com/26924023/32182377-17089da0-bdc9-11e7-9fb9-8ebbcc0414c9.png)](https://www.facebook.com/kenshi.hao)
:---:|:---:|:---:|:---:
[Trần Lục Long Tính](https://github.com/tinhdk1) | [Hoàng Công Kiên](https://github.com/deepink2) | [Huỳnh Vân Nhật](https://github.com/huynhvannhat) | [Trần Văn Dân](https://github.com/trandan27/)

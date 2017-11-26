4324nhom15

Bài tập nhóm Môn học Các hệ thống phân tán

Các hệ thống phân tán

Bài tập nhóm Môn học Các hệ thống phân tán  

Các phần mềm cần thiết  

Xampp
Eclipse IDE for Java Developers
Flyway and Maven Plugin
Tìm hiểu về Flyway

Flyway là gì!?

Flyway là một java open source library hỗ trợ migrate data cho các ứng dụng, một khi chúng ta cần:
- Nâng cấp database khi thay đổi cấu trúc hoặc dữ liệu.
- Quản lý lịch sử thay đổi version một cách chặt chẽ.
- Thực thi migrating một cách tự động.
- Đồng bộ data structure giữa các server development.
Hỗ trợ hầu hết các relational database:

List Relational Database

Flyway hoạt động như thế nào

Flyway tạo ra một table có tên SCHEMA_VERSION dùng để quản lý lịch sử phiên bản cũng như trạng thái của database.
Database changed

Tích hợp Flyway Maven Plugin

Tạo maven project:

# Tạo java console app sử dụng maven từ command line hoặc IDE:

mvn archetype:generate -B \
        -DarchetypeGroupId=org.apache.maven.archetypes \
        -DarchetypeArtifactId=maven-archetype-quickstart \
        -DarchetypeVersion=1.1 \
        -DgroupId=flyway-maven-sample \
        -DartifactId=flyway-maven-sample \
        -Dversion=1.0-SNAPSHOT \
        -Dpackage=manhnv.flyway.sample
Add Jdbc Driver Dependency:

# Thêm Dependencies vào file Pom.xml
<dependencies>
        <!--Add postgres jdbc driver-->
        <dependency>
            <groupId>postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <version>9.1-901.jdbc4</version>
        </dependency>
    </dependencies>
Tài liệu tham khảo online

Migration data với Flyway sử dụng Maven: Giới thiệu về Flyway và cách sử dụng flyway với Maven.
How to integrate Flyway on Maven: Cách tích hợp Maven với Flyway.
Phân chia thực hiện

Cả nhóm cùng thự hiện nghiên cứu Flyway trong giai đoạn 1.

Nhóm

Danh sách nhóm sinh viên thực hiện:

Trần Lục Long Tính	Hoàng Công Kiên	Huỳnh Vân Nhật	Trần Văn Dân
Trần Lục Long Tính	Hoàng Công Kiên	Huỳnh Vân Nhật	Trần Văn Dân

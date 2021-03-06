#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_Button_FileSelect_released();

    void on_pushButton_released();

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H

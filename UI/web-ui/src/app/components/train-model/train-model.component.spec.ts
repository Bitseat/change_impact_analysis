import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainModelComponent } from './train-model.component';

import { DragdropService } from "../dragdrop.service";
import { HttpEvent, HttpEventType } from '@angular/common/http';
import { DomSanitizer } from '@angular/platform-browser';


describe('TrainModelComponent', () => {
  let component: TrainModelComponent;
  let fixture: ComponentFixture<TrainModelComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TrainModelComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainModelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
